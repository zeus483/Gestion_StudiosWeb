from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...db import SessionLocal
from passlib.context import CryptContext
from ...models.account import Account
from ...schemas.account import AccountCreate
from ...crud import accounts_crud 
from typing import List
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/accounts")
def get_account(db : Session = Depends(get_db)):
    models = accounts_crud.get_accounts(db=db)
    return models

@router.post("/createAccount")
def create_account(account : AccountCreate,db: Session = Depends(get_db)):
    return accounts_crud.createModel(db=db, account=account)

@router.delete("/deleteAccount/{account_id}", response_model= AccountCreate)
def delete_account(account_id: int, db: Session = Depends(get_db)):
    account = accounts_crud.delete_account(db=db, account_id=account_id)
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return account