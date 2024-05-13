from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate
from ..schemas.user_update import UserUpdate
from ..schemas.change_password import PasswordChange
from passlib.context import CryptContext
#funciones utiles
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#get one user with his username 
def get_user(db: Session, username : str):
    return db.query(User).filter(User.username == username).first()
#get all user, you can skipy and limit the result
def get_users(db: Session, skip : int =0, limit : int = 100): 
    return db.query(User).offset(skip).limit(limit).all()
#you can create a new user
def create_user(db: Session, user :  UserCreate):
    db_user = User(username = user.username, hashed_password = user.hashed_password, role = user.rol, is_active = user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, username: str, user_update: UserUpdate):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        return None  
    user_data = user_update.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    return db_user

def change_user_password(db: Session, username: str, current_password: str, new_password: str):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user and pwd_context.verify(str(current_password), str(db_user.hashed_password)):
        hashed_new_password = pwd_context.hash(new_password)
        db_user.hashed_password = hashed_new_password
        db.commit()
        return True
    return None       

def autentify_password(db: Session, usermane: str, password :  str):
    db_user  = db.query(User).filter(User.username == usermane).first()
    print(db_user)
    return pwd_context.verify(str(password),db_user.hashed_password)

#traer los usuarios de categoria modelo y activos 
def get_active_models(db: Session):
    return db.query(User).filter(User.is_active == True, User.role == 'Modelo').all()
