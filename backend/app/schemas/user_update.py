from typing import Optional
from pydantic import BaseModel, EmailStr

class UserUpdate(BaseModel):
    username: Optional[str] = None
    rol : Optional[str] = None
    is_active: Optional[bool] = None
