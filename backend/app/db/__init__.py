# backend/app/db/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base  # Importa la clase base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # URL de conexión a la base de datos SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)  # Crea todas las tablas basadas en los modelos
