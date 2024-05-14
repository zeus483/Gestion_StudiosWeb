from pydantic import BaseModel

class ModelProgress(BaseModel):
    username: str
    id : int
    token_goal: int
    tokens_generated: int
    tokens_faltantes: int