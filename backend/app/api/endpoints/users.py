from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from ...db import SessionLocal
from passlib.context import CryptContext
from ...models.user import User
from ...schemas.user import UserCreate
from ...crud import users_crud 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

@router.post("/create_new_user")
def create_new_user( user: UserCreate,db: Session = Depends(get_db)):
    db_user = users_crud.get_user(db,username= user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashepassword = pwd_context.hash(user.hashed_password)
    user.hashed_password = hashepassword
    return users_crud.create_user(db=db, user=user)
@router.post("/user_id")
def get_user(users:str,db: Session=Depends(get_db)):
    db_user = users_crud.get_user(db,username= users)
    if not db_user:
        raise HTTPException(status_code=400, detail="Username not found")
    return db_user