from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base
from .page import Page
from .model import Model

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    page = Column(String, ForeignKey('pages.url'))
    user_model = Column(String, ForeignKey('users.username'))
    password = Column(String, nullable=False)
    model_name = Column(String, ForeignKey('models.name'))
    pages = relationship("Page", back_populates="accounts")
    user = relationship("User", back_populates="accounts")
    model = relationship("Model", back_populates="accounts")