from datetime import datetime

from pydantic import BaseModel, Field, field_validator
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase


class OrderValidationModel(BaseModel):
    pass

# Современный стиль SQLAlchemy 2.0, который нативно понимает Mypy
class Base(DeclarativeBase):
    pass

class DBOrder(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
