from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base
from ..models.page import Page
from ..models.user import User

class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    name_page = Column(String, ForeignKey('pages.name'))
    tokens = Column(Integer, default=0)
    pages = relationship("Page", back_populates="tokens")
    user = relationship("User", back_populates="tokens")