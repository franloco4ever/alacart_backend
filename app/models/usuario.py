from datetime import datetime
from sqlalchemy import Column, Integer, String
from app.database import Base

class Usuario(Base):
  __tablename__ = "usuarios"
  
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  nombre = Column(String(100), nullable=False)
  email = Column(String(255), unique=True, index=True, nullable=False)
  hashed_pass = Column(String(255), nullable=False)
  admin = Column(Boolean, default=False, nullable=False)
  created_at = Column(DateTime, default=datetime.now, nullable=False)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)