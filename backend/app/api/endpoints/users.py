from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...db import SessionLocal
from passlib.context import CryptContext
from ...models.user import User
from ...schemas.user import UserCreate
from ...schemas.user_update import UserUpdate
from ...schemas.change_password import PasswordChange
from ...crud import users_crud 
from ...schemas.credentials import LoginCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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
@router.get("/user_id")
def get_user(users:str,db: Session=Depends(get_db)):
    db_user = users_crud.get_user(db,username= users)
    if not db_user:
        raise HTTPException(status_code=400, detail="Username not found")
    return db_user

@router.put("/users/{username}", response_model= UserUpdate)
def update_user(username: str, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = users_crud.update_user(db, username=username, user_update=user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.post("/change-password/")
def change_password(request: PasswordChange, db: Session = Depends(get_db)):
    updated_user = users_crud.change_user_password(
        db=db,
        username=request.username,
        current_password=request.current_password,
        new_password=request.new_password
    )
    if updated_user is None:
        raise HTTPException(status_code=400, detail="Invalid current password or username does not exist")
    return updated_user

@router.post("/login")
async def login(form_data: LoginCredentials, db: Session = Depends(get_db)):
    user_authenticated = users_crud.autentify_password(db, form_data.username, form_data.password)
    if not user_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    db_user = users_crud.get_user(db,form_data.username)
    return {"access": True, "user_info": db_user}
