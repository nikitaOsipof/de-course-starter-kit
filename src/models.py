from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
class OrderValidationModel(BaseModel): pass
Base = declarative_base()
class DBOrder(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
