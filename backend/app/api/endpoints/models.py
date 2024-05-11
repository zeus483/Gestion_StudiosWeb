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
def read_users():
    return {"message": "Fetching all models"}