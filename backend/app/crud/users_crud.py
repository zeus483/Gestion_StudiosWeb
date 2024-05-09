from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate

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