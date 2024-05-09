from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..db.base import Base
from .account import Account
from .model import Model

class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    models = relationship("Model", back_populates="users")
    accounts = relationship("Account", back_populates="users")