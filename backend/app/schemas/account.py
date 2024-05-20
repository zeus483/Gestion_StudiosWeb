from pydantic import BaseModel
class AccountCreate(BaseModel):
    password: str
    model_name : str
    page : str
    user_model: str
    