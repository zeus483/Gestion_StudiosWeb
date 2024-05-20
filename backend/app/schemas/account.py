from pydantic import BaseModel
from typing import Optional
class AccountCreate(BaseModel):
    password: str
    model_name : str
    page : str
    user_model: str
    api_token : Optional[str] = None
    