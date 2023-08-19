from sqlalchemy import Boolean, Column, Integer, TIMESTAMP, ForeignKey, BOOLEAN, DATETIME
from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class CourseAttractions(Base):
    __tablename__ = "course_attractions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    attraction_id = Column(Integer, ForeignKey('attractions.id'))
    order_num = Column(Integer)
    is_last = Column(Boolean)
    departure_time = Column(TIMESTAMP)

    # CourseAttractions와 Course 간의 다대일 관계 설정
    # course = relationship("Course", back_populates="attractions")
    
    # CourseAttractions와 Attraction 간의 다대일 관계 설정
    # attraction = relationship("Attraction")