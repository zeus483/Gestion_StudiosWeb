from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from ...db import SessionLocal
from passlib.context import CryptContext
from ...models.user import User
from ...schemas.user import UserCreate
from ...crud import users_crud 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
router = APIRouter()

@router.get("/users")
def read_users(db : Session = Depends(get_db)):
    users = users_crud.get_users(db=db)
    return users
