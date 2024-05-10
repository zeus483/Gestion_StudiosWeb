from pydantic import BaseModel, Field

class PasswordChange(BaseModel):
    username: str
    current_password: str 
    new_password: str 
