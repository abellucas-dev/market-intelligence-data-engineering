readme_content = """# 📊 Market Intelligence & Data Job Monitor

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red.svg)](https://www.sqlalchemy.org/)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-0594D0.svg?logo=spacy&logoColor=white)](https://spacy.io/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF.svg?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2.svg?logo=discord&logoColor=white)](https://discord.com/)

Um produto de dados inteligente e *end-to-end* projetado para monitorar autonomamente o mercado brasileiro de Engenharia e Ciência de Dados. O sistema orquestra desde a coleta bruta de dados públicos até a análise semântica descritiva e entrega automatizada de alertas de vagas em tempo real.

---

## 🏗️ Arquitetura e Fluxo do Pipeline

O sistema opera de forma serverless e orientada a estado, seguindo o fluxo abaixo:

```text
[ LinkedIn ] ──(Web Scraping)──> [ Python Scraper ]
                                        │
                                (Deduplicação ORM)
                                        ▼
                               [ SQLite Database ] <──> [ FastAPI Backend ]
                                        │
                                (Filtro de Estado)
                                        ▼
     [ Discord Mobile ] <──(Webhooks)───┤ (Se vaga ideal e inédita: Python + Spark)
                                        ▼
                                [ Análise NLP ] ──(Matplotlib)──> [ Top 10 Skills Chart ]

Ingestão (Scraping): Robô construído com requests e BeautifulSoup faz varreduras geolocalizadas no LinkedIn utilizando técnicas de conformidade de rede (polite crawling).

Armazenamento e Estado: Os dados brutos são tratados e inseridos em um banco de dados relacional SQLite utilizando o ORM SQLAlchemy. O pipeline valida se o link da vaga já existe para evitar duplicidade.

Serviço de API: Uma camada de backend estruturada em FastAPI disponibiliza endpoints dinâmicos (/vagas) que servem o banco em formato JSON padronizado.

Inteligência Artificial (NLP): Processamento de Linguagem Natural nativo com a biblioteca spaCy realiza a limpeza profunda das descrições (remoção de stop words, pontuações e normalização) para traçar o mapa estatístico real das habilidades exigidas pelo mercado.

Automação e Orquestração: Um motor de CI/CD via GitHub Actions roda em cron-job diário (às 06:00 BRT). A máquina virtual persiste o estado do banco (.db) de volta no repositório de forma nativa e segura.

Sistema de Alerta Dinâmico: Caso uma vaga seja inédita e contenha a intersecção ideal de tecnologias chaves (ex: Python + Spark), um gatilho via Discord Webhook dispara uma notificação rica e instantânea diretamente no dispositivo móvel do usuário.

🚀 Funcionalidades Chave
Coleta Autônoma Sem Custos: Execução agendada 100% gratuita rodando na infraestrutura em nuvem da Microsoft via GitHub Actions.

Segurança de Credenciais: Links e tokens de comunicação sensíveis protegidos via criptografia através do GitHub Repository Secrets.

Controle de Spam (Stateful Control): Diferente de bots tradicionais, este sistema lembra do histórico e só incomoda o usuário quando uma oportunidade ouro realmente nova surge no mercado.

Análise Semântica de Alta Precisão: Gráficos analíticos gerados com Matplotlib descartam termos genéricos e focam no verdadeiro core técnico das contratações atuais.

📂 Estrutura do Projeto
├── .github/workflows/
│   └── rotina_scraper.yml    # Arquivo de orquestração e cron-job da Nuvem
├── database.py               # Configuração do banco SQLite, Modelos ORM e Sessão
├── main.py                   # Backend e endpoints REST com FastAPI
├── scraper_linkedin.py       # Engine de coleta integrada com banco e Webhooks
├── fase3_nlp.py              # Pipeline de Processamento de Linguagem Natural e Gráficos
├── vagas_tech.db             # Banco de dados relacional que mantém o estado da aplicação
├── .gitignore                # Proteção técnica para exclusão de caches e ambientes virtuais
└── README.md                 # Documentação executiva do produto

🛠️ Como Executar Localmente
Pré-requisitos
Python 3.11 ou superior instalado.

Criar e configurar um Webhook em um canal privado no Discord.

Passos para Instalação
Clone este repositório:
git clone [https://github.com/abellucas-dev/market-intelligence-data-engineering.git](https://github.com/abellucas-dev/market-intelligence-data-engineering.git)
cd market-intelligence-data-engineering.git

Crie e ative seu ambiente virtual:
python -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\\\\Scripts\\\\activate

Instale as dependências essenciais:
pip install requests beautifulsoup4 pandas sqlalchemy fastapi uvicorn spacy matplotlib
python -m spacy download pt_core_news_sm

Configure a sua URL do webhook do Discord como variável de ambiente local ou insira diretamente no script para testes locais:
export DISCORD_WEBHOOK_URL="sua_url_aqui" # No Windows (CMD): set DISCORD_WEBHOOK_URL="sua_url_aqui"

Inicialize a API de dados:
uvicorn main:app --reload

Acesse os dados estruturados em seu navegador em: http://127.0.0.1:8000/vagas

Execute o script analítico de NLP:
python fase3_nlp.py

📈 Inteligência de Mercado Gerada
O gráfico abaixo exemplifica a extração semântica realizada pelo módulo de NLP do projeto após a filtragem profunda de ruídos textuais:


<img width="640" height="559" alt="grafico_skills" src="https://github.com/user-attachments/assets/8c96fafe-d56c-4bc2-a0df-c041801b463e" />

📝 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para clonar, estudar e aprimorar o fluxo do pipeline.
"""
