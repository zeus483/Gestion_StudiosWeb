from fastapi import FastAPI
from .api.endpoints import users, models, account,tests,pages# Importa los módulos de endpoint
from .api.endpoints.tests import router as test_db_router
from .core.config import settings  # Importa configuraciones si es necesario
from .db import engine  # Importa el motor de la base de datos
from .db.base import Base
import logging
from fastapi.middleware.cors import CORSMiddleware# Importa Base para la creación de tablas
app= FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origenes, ajusta según tus necesidades
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los encabezados
)
logging.basicConfig(level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
@app.get("/")
def read_root():
    return {"Hellow": "world"}
app.include_router(users.router)
app.include_router(models.router)
app.include_router(pages.router)
app.include_router(account.router)
app.include_router(test_db_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
