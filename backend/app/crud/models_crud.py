from sqlalchemy.orm import Session
from sqlalchemy.sql import func, case
from ..models.model import Model
from ..schemas.model import CreateModel
from ..schemas.model_update import ModelUpdate
from .users_crud import get_user

#funcion para optener una modelo por el id
def get_model_id(db: Session, id : int):
    return db.query(Model).filter(Model.id == id).first()

#traer las modelos con un combre de usuario
def get_model_username(db : Session, username : str):
    return db.query(Model).filter(Model.username == username).all()
#optener modelo por email
def get_models_by_email(db: Session, email: str):
    return db.query(Model).filter(Model.email == email).all()

#traer todas las modelos
def get_models(db: Session, skip : int = 0, limit : int = 100):
    return db.query(Model).offset(skip).limit(limit).all()

#crear un nuevo registro de una modelo
def create_model(db: Session, model : CreateModel):
    db_user = get_user(db,username= model.username)
    if db_user:
        db_model = Model(username = model.username,name = model.name, email = model.email, phone = model.phone, number_account = model.number_account, type_account = model.type_account, connection_hours = model.connection_hours)
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        return db_model
    return None
#funcion para modificar el registro de una modelo
def update_model(db: Session, model_id: int, model_update: ModelUpdate):
    db_model = db.query(Model).filter(Model.id == model_id).first()
    if db_model:
        for key, value in model_update.dict(exclude_unset=True).items():
            setattr(db_model, key, value)
        db.commit()
        db.refresh(db_model)
        return db_model
    return None

#funcion para eliminar una modelo
def delete_model(db: Session, model_id: int):
    db_model = db.query(Model).filter(Model.id == model_id).first()
    if db_model:
        db.delete(db_model)
        db.commit()
        return True
    return False


def get_model_progress(db: Session):
    # Calcula los tokens faltantes, ajustando valores negativos a cero usando una expresión CASE en lugar de GREATEST
    token_goal = func.coalesce(Model.token_goal, 0)
    tokens_generated = func.coalesce(Model.tokens_generated, 0)
    tokens_faltantes = case(
        (token_goal - tokens_generated >= 0, token_goal - tokens_generated),
        else_=0
    )

    # Realiza la consulta seleccionando las columnas específicas y la columna calculada
    return db.query(
        Model.username,
        Model.id,
        token_goal.label("token_goal"),
        tokens_generated.label("tokens_generated"),
        tokens_faltantes.label("tokens_faltantes")
    ).all()
    
    