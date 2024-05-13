from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from ..db.base import Base
from .model_history import ModelHistory

class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey('users.username'))
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    type_account = Column(String, nullable=False)
    number_account = Column(String(12), nullable=False)
    tokens_generated = Column(Integer, default=0)
    connection_hours = Column(Float, default=0.0)
    token_goal = Column(Integer)
    rest_days = Column(Date)
    follower_growth = Column(Integer, default=0)
    user = relationship("User", back_populates="models")
    accounts = relationship("Account", back_populates="model")
    model_history = relationship("ModelHistory", back_populates="model")

class FinancialRecord(Base):
    __tablename__ = 'financial_records'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey('models.id'))
    tokens = Column(Integer)
    usd_amount = Column(Float)
    local_currency_amount = Column(Float)
    exchange_rate = Column(Float)
    date = Column(Date)
    model = relationship("Model", back_populates="financial_records")

Model.financial_records = relationship("FinancialRecord", back_populates="model", order_by=FinancialRecord.date)
