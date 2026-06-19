from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Vaga, init_db
from fastapi import Query
from typing import Optional

app = FastAPI()

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/vagas")
def listar_vagas(localizacao: Optional[str] = None, 
    empresa: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Vaga)
    
    if localizacao:
        query = query.filter(Vaga.localizacao.contains(localizacao))
    if empresa:
        query = query.filter(Vaga.empresa.ilike(f"%{empresa}%"))
        
    return query.all()

@app.get("/vagas/{skill}")
def buscar_por_skill(skill: str, db: Session = Depends(get_db)):
    return db.query(Vaga).filter(Vaga.descricao.contains(skill)).all()