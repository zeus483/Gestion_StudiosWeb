from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..db.base import Base
from .account import Account
from .model import Model
from .tokens import Tokens

class User(Base):
    __tablename__ = 'users'
    username = Column(String, unique=True, primary_key=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    models = relationship("Model", back_populates="user")
    accounts = relationship("Account", back_populates="user")
    tokens = relationship("Tokens", back_populates= "user")
    