# backend/app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Crea una clase base de la cual heredarán todos los modelos
