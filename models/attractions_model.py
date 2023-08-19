from datetime import datetime
from sqlalchemy.orm import relationship

from sqlalchemy import Boolean, Float, DateTime, Column, Integer, String, ForeignKey, DateTime
from config.database import Base
from sqlalchemy.sql import func

class Attractions(Base):
    __tablename__ = "attractions"


    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(45), nullable=False)
    description = Column(String(45), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, default=func.now())

    # Define a relationship to CourseAttractions if needed
    # course_attractions = relationship("CourseAttractions", back_populates="attraction")

    def __repr__(self):
        return f"<Attractions(id={self.id}, name={self.name}, description={self.description})>"