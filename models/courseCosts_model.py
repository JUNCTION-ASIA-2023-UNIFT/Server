from sqlalchemy import Boolean, Column, Integer, Float, BOOLEAN, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from config.database import Base

class CourseCost(Base):
    __tablename__ = "course_cost"

    id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    cost = Column(Float)
    is_selected = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # CourseCost와 User 간의 다대일 관계 설정
    # driver = relationship("User", back_populates="courses")
    
    # CourseCost와 Course 간의 다대일 관계 설정
    # course = relationship("Course", back_populates="costs")