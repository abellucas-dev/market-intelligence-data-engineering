from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Conexão com o banco SQLite
DATABASE_URL = "sqlite:///./vagas_tech.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição da Tabela
class Vaga(Base):
    __tablename__ = "vagas"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    empresa = Column(String)
    localizacao = Column(String)
    link = Column(String)
    descricao = Column(Text)
    data_coleta = Column(DateTime, default=datetime.datetime.utcnow)

# Criar as tabelas no banco
def init_db():
    Base.metadata.create_all(bind=engine)