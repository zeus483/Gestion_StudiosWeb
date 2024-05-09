from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    page = Column(String, ForeignKey('pages.url'))
    user = Column(String, ForeignKey('users.username'))
    password = Column(String, nullable=False)
    model_name = Column(String, ForeignKey('models.name'))
    page = relationship("Page", back_populates="accounts")
    user = relationship("User", back_populates="accounts")
    model = relationship("Model", back_populates="accounts")