from fastapi import FastAPI
from .api.endpoints import users, models, sessions, notes  # Importa los módulos de endpoint
from .core.config import settings  # Importa configuraciones si es necesario
from .db.session import engine  # Importa el motor de la base de datos
from .db.base_class import Base  # Importa Base para la creación de tablas