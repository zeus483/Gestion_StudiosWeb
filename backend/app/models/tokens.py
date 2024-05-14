from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base
from ..models.account import Account


class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    name_page = Column(String, ForeignKey('accounts.page'))
    tokens = Column(Integer, default=0)
    accounts = relationship("Account", back_populates="tokens")
    user = relationship("User", back_populates="tokens")