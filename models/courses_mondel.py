from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tourist_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255))
    category = Column(String(255))
    reservation_time = Column(DATETIME)
    status = Column(String(45))
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())

    # Course와 User 간의 다대일 관계 설정
    # tourist = relationship("User", back_populates="courses")
    
    # Course와 CourseCost 간의 일대다 관계 설정
    # costs = relationship("CourseCost", back_populates="course")
    
    # Course와 CourseAttractions 간의 일대다 관계 설정
    # attractions = relationship("CourseAttractions", back_populates="course")
