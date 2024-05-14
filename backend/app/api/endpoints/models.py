from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...db import SessionLocal
from passlib.context import CryptContext
from ...models.model import Model
from ...schemas.model import CreateModel
from ...schemas.model_update import ModelUpdate
from ...crud import models_crud 
from ...schemas.credentials import LoginCredentials
from ...schemas.model_progress import ModelProgress
from typing import List
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
def delete_model(id: int, db: Session = Depends(get_db)):
    if not models_crud.delete_model(db, id):
        raise HTTPException(status_code=404, detail="Model not found")
    return {"detail": "Model deleted successfully"}

@router.put("/update_model/{id}")
def update_model(id: int, model_update: ModelUpdate, db: Session = Depends(get_db)):
    updated_model = models_crud.update_model(db, id, model_update)
    if updated_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return updated_model


@router.get("/models/{id}")
def read_model(id: int, db: Session = Depends(get_db)):
    model = models_crud.get_model_id(db, id)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@router.get("/models/by_username/{username}")
def get_model_by_username(username: str, db: Session = Depends(get_db)):
    model = models_crud.get_model_username(db, username)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@router.get("/models/by_email/{email}")
def get_model_by_email(email: str, db: Session = Depends(get_db)):
    model = models_crud.get_models_by_email(db, email)
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model

@router.get("/models-and-goals", response_model=List[ModelProgress])
def get_models_and_goals(db: Session = Depends(get_db)):
    models = models_crud.get_model_progress(db=db)
    return models
