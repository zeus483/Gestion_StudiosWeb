from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...db import SessionLocal
from passlib.context import CryptContext
from ...models.model import Model
from ...schemas.model import CreateModel
from ...schemas.model_update import ModelUpdate
from ...crud import models_crud 
from ...schemas.credentials import LoginCredentials
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/models")
def read_models(db : Session = Depends(get_db)):
    users = models_crud.get_models(db=db)
    return users
@router.post("/createModel")
def create_new_user( model: CreateModel,db: Session = Depends(get_db)):
    return models_crud.create_model(db=db, model=model)

@router.delete("/delete_model/{id}")
def delete_model(id : int, db : Session = Depends(get_db)):
    return models_crud.delete_model(db,id)