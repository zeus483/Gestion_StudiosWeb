from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base


class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    type_account = Column(String, nullable=False)
    number_account = Column(String(12), nullable=False)
    user = relationship("User", back_populates="models")
    accounts = relationship("Account", back_populates="model")