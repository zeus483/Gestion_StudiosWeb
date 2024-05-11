from typing import Optional
from pydantic import BaseModel

class LoginCredentials(BaseModel):
    username: Optional[str] = None
    password : Optional[str] = None
