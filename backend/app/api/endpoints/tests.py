from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ...db import SessionLocal
from ...models.model import Model

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/get-model-columns-test/")
def get_model_columns(db: Session = Depends(get_db)):
    # Obtener las columnas del modelo Model
    column_names = [column.name for column in Model.__table__.columns]
    return {"columns": column_names} 