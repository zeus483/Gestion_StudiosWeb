from pydantic import BaseModel

class CreateModel(BaseModel):
    username: str
    name: str
    email: str
    phone: str
    type_account: str
    number_account: str