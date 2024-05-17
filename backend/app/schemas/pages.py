from pydantic import BaseModel

class CreatePage(BaseModel):
    url : str
    name : str
    