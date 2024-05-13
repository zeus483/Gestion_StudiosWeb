from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..db.base import Base
from datetime import datetime

class ModelHistory(Base):
    __tablename__ = 'model_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('models.id'))
    tokens_generated = Column(Integer)
    token_goal = Column(Integer)
    period_end_date = Column(DateTime, default=datetime.utcnow)
    model = relationship("Model", back_populates="model_history") 

