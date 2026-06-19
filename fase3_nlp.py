import requests
import pandas as pd
import spacy
from collections import Counter
import matplotlib.pyplot as plt

nlp = spacy.load("pt_core_news_sm")

url = "http://127.0.0.1:8000/vagas"
vagas = requests.get(url).json()

texto_completo = " ".join([vaga['descricao'] for vaga in vagas])
doc = nlp(texto_completo.lower())

keywords = [token.text for token in doc if token.is_alpha and not token.is_stop and len(token.text) > 2]

tecnologias_alvo = ['python', 'sql', 'aws', 'azure', 'spark', 'docker', 'airflow', 'dbt', 'gcp', 'java', 'pandas', 'git']
contagem = Counter([word for word in keywords if word in tecnologias_alvo])

df = pd.DataFrame(contagem.most_common(10), columns=['Habilidade', 'Frequencia'])
df.set_index('Habilidade').plot(kind='barh', color='darkblue')
plt.title('Top 10 Habilidades - Análise NLP')
plt.show()