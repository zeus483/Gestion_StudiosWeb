from sqlalchemy.orm import Session
from ..models.model import Model
from ..schemas.model import CreateModel
from ..schemas.model_update import ModelUpdate

#funcion para optener una modelo por el id
def get_model_id(db: Session, id : int):
    return db.query(Model).filter(Model.id == id).first()

#traer las modelos con un combre de usuario
def get_model_username(db : Session, username : str):
    return db.query(Model).filter(Model.username == username)

#traer las modelos con 