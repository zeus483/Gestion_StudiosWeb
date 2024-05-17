from sqlalchemy.orm import Session
from ..models.page import Page
from ..schemas.pages import CreatePage


#funcion para traer las paginas que tengo activas
def get_pages(db: Session, skip : int = 0, limit : int = 100):
    return db.query(Page).offset(skip).limit(limit).all()

#funcion para agregar una nueva pagina
def create_pages(db: Session, page : CreatePage):
    new_page = Page(url=page.url,name=page.name)
    db.add(new_page)
    db.commit()
    db.refresh(new_page)
    return new_page

