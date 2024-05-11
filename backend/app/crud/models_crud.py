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

#traer todas las modelos
def get_model(db: Session, skip : int = 0, limit : int = 100):
    return db.query(Model).offset(skip).limit(limit).all()

#crear un nuevo registro de una modelo
def create_model(db: Session, model : CreateModel):
    db_model = Model(usename = model.username,name = model.name, email = model.email, phone = model.phone, number_account = model.number_account, type_account = model.type_accuount)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model
