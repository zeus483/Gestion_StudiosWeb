from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    hashed_password : str
    rol : str
    is_active: bool
    