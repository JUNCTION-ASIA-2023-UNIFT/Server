from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    role = Column(String(45))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    
    # courses = relationship("Course", back_populates="tourist")