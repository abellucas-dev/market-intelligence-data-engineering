import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from database import SessionLocal, Vaga, init_db
import os

DISCORD_WEBHOOK_URL = os.environ.get("https://discord.com/api/webhooks/1517162773950234715/2zGA3YbeNOeDXRN6yEhftq1-r5dMJc4kHVCNldpLX2q-3cAWkhh4lshJE2cuYAc8Qsyz")

init_db()

def enviar_alerta_discord(titulo, empresa, localizacao, link):
    mensagem = {
        "content": f"🚨 **NOVA VAGA IDEAL ENCONTRADA!** 🚨\n\n"
                   f"💼 **Cargo:** {titulo}\n"
                   f"🏢 **Empresa:** {empresa}\n"
                   f"📍 **Local:** {localizacao}\n"
                   f"🔗 **Link:** {link}"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=mensagem)
    except Exception as e:
        print(f"Erro ao enviar alerta para o Discord: {e}")

def salvar_vaga_no_banco(titulo, empresa, localizacao, link, descricao):
    db = SessionLocal()
    vaga_existente = db.query(Vaga).filter(Vaga.link == link).first()
    
    foi_salva = False
    if not vaga_existente:
        nova_vaga = Vaga(
            titulo=titulo, 
            empresa=empresa, 
            localizacao=localizacao, 
            link=link, 
            descricao=descricao
        )
        db.add(nova_vaga)
        db.commit()
        foi_salva = True  
    db.close()
    return foi_salva

def buscar_vagas_linkedin(cargo):
    print(f"Iniciando busca por vagas de '{cargo}' no Brasil...")
    cargo_formatado = cargo.replace(' ', '%20')
    url = f"https://www.linkedin.com/jobs/search?keywords={cargo_formatado}&location=Brazil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
    }
    
    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200:
        print(f"Erro ao acessar a listagem. Código: {resposta.status_code}")
        return
    
    soup = BeautifulSoup(resposta.text, 'html.parser')
    vagas_html = soup.find_all('div', class_='base-card')
    
    vagas_para_processar = vagas_html[:60]
    print(f"Encontradas vagas. Iniciando extração de detalhes das {len(vagas_para_processar)} primeiras...")

    for i, vaga in enumerate(vagas_para_processar, start=1):
        try:
            titulo = vaga.find('h3', class_='base-search-card__title').text.strip()
            empresa = vaga.find('h4', class_='base-search-card__subtitle').text.strip()
            localizacao = vaga.find('span', class_='job-search-card__location').text.strip()
            link = vaga.find('a', class_='base-card__full-link')['href']
            
            print(f"[{i}/{len(vagas_para_processar)}] Acessando detalhes da vaga na {empresa}...")
            resposta_vaga = requests.get(link, headers=headers)
            
            descricao = "Não encontrada"
            if resposta_vaga.status_code == 200:
                soup_vaga = BeautifulSoup(resposta_vaga.text, 'html.parser')
                tag_descricao = soup_vaga.find('div', class_='show-more-less-html__markup')
                if tag_descricao:
                    descricao = tag_descricao.get_text(separator="\n").strip()
            else:
                print(f"      Aviso: Não foi possível acessar esta vaga específica. Código: {resposta_vaga.status_code}")
            
            eh_vaga_nova = salvar_vaga_no_banco(titulo, empresa, localizacao, link, descricao)

            if eh_vaga_nova:
                print("Vaga salva com sucesso no banco de dados SQLite!")
                
                if "python" in descricao.lower() and "spark" in descricao.lower():
                    print(f"🔥 Vaga ideal e inédita na {empresa}! Disparando o Discord...")
                    enviar_alerta_discord(titulo, empresa, localizacao, link)
            else:
                print("Vaga já existia no banco de dados. Alerta pulado.")
            
            time.sleep(3)
            
        except AttributeError:
            continue

    print("\nProcesso concluído com sucesso!")

buscar_vagas_linkedin("Engenharia de Dados")