from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import Optional


from config.database import SessionLocal

from models.attractions_model import Attractions
# from . import schemas, services
from schemas.courses_schemas import CreateCourse, AttractionInfo
from services import courses_services


router = APIRouter()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/attractions/")
def get_attractions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(Attractions).all()


@router.get("/courses/")
async def get_courses(

    category: str = Query(None, description="Filter courses by category", min_length=1),
    db: Session = Depends(get_db),
):

    courses = courses_services.get_courses_with_tour_list(db, category)
    return courses


@router.get("/courses/{course_id}/")
async def get_course_details(
    course_id: int,
    db: Session = Depends(get_db)
):
    course_details = courses_services.get_course_details(db, course_id)
    if not course_details:
        return {"message": "Course not found"}
    return course_details


@router.get("/courses/mycourses/{tourist_id}/")
async def get_my_course_list(
    tourist_id: int,
    db: Session = Depends(get_db)
):
    course_list = courses_services.get_my_course_list(db, tourist_id)
    if not course_list:
        return {"message": "Course Exsist"}
    return course_list


@router.post("/courses/")
async def create_course(course_info: CreateCourse, db: Session = Depends(get_db)):

    course_id = courses_services.create_course(db, course_info)

    if course_id is None:
        raise HTTPException(status_code=400, detail="Failed to create the course")

    return {"message": "Course created successfully", "course_id": course_id}


@router.get("/recent-course-costs/{tourist_id}/")
async def get_course_costs_route(
    tourist_id: int,
    db: Session = Depends(get_db)
):
    course_costs = courses_services.get_course_costs(db, tourist_id)
    return course_costs

@router.post("/execute-trade/{tourist_id}/")
async def execute_trade_route(tourist_id: int, db: Session = Depends(get_db)):
    return courses_services.execute_trade(db, tourist_id)