from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..db.base import Base

class Page(Base):
    __tablename__ = 'pages'
    url = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    accounts = relationship("Account", back_populates="pages")