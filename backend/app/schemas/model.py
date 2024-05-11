from pydantic import BaseModel

class CreateModel(BaseModel):
    username: str
    name: str
    email: str
    phone: str
    type_accuount: str
    number_account: str