from sqlalchemy.orm import Session
from sqlalchemy.sql import func, case
from sqlalchemy.exc import SQLAlchemyError
from ..models.account import Account
from ..schemas.account import AccountCreate

#funcion para optener las cuentas actuales
def get_accounts(db: Session, skip : int = 0, limit : int = 100):
    return db.query(Account).offset(skip).limit(limit).all()

#funcion para crear una modelo
def createModel(db:Session, account: AccountCreate):
    new_account = Account(
        password = account.password, 
        model_name = account.model_name, 
        page = account.page, 
        user_model = account.user_model,
        api_token = account.api_token)

    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account 

# Función para eliminar una cuenta
def delete_account(db: Session, account_id: int):
    try:
        account = db.query(Account).filter(Account.id == account_id).first()
        if account:
            db.delete(account)
            db.commit()
            return account
        else:
            return None
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError(f"Error al eliminar la cuenta: {e}")