from fastapi import APIRouter,HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...db import SessionLocal
from ...models.page import Page
from ...schemas.pages import CreatePage
from ...crud import pages_crud
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/pages")
def read_models(db : Session = Depends(get_db)):
    pages = pages_crud.get_pages(db=db)
    return pages

@router.post("/add-page")
def add_page(page : CreatePage, db: Session = Depends(get_db)):
    return pages_crud.create_pages(db,page)