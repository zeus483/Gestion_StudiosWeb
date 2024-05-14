from typing import Optional
from pydantic import BaseModel, EmailStr

class ModelUpdate(BaseModel):
    username: Optional[str] = None
    name : Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    type_accuount: Optional[str] = None
    number_account: Optional[str] = None
    connection_hours : Optional[float] = None
    token_goal : Optional[int] = None
