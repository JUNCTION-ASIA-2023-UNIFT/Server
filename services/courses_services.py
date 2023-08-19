
from sqlalchemy.orm import Session
from models.courses_mondel import Course
from models.attractions_model import Attractions
from models.courseAttraction_model import CourseAttractions
from models.users_model import User
from models.courseCosts_model import CourseCost
from sqlalchemy import desc

from schemas.courses_schemas import CreateCourse, AttractionInfo

def get_recommended_courses_list(db: Session):
    query = db.query(Course)
    query = query.filter(Course.tourist_id == 1)

    courses = query.all()
    return courses


def get_courses_with_tour_list(db: Session, category: str = None):
    query = db.query(Course)

    if category:
        print("i got a category filter")
        query = query.filter(Course.category == category)


    courses = query.all()

    if not courses:
        return []  
    course_ids = [course.id for course in courses]
    attraction_ids = db.query(CourseAttractions.attraction_id).filter(CourseAttractions.course_id.in_(course_ids)).all()

    if not attraction_ids:
        return []  

    attraction_ids = [attraction_id for (attraction_id,) in attraction_ids]

    attractions = db.query(Attractions).filter(Attractions.id.in_(attraction_ids)).all()

    courses_with_tour_list = []
    for course in courses:
        tour_list = []

        for attraction in attractions:
            if attraction.id in attraction_ids:
                tour_list.append({
                    "attraction_id": attraction.id,
                    "name": attraction.name,
                    "description": attraction.description,
                    "latitude": attraction.latitude,
                    "longitude": attraction.longitude,
                })

        course_data = {
            "category": course.category,
            "id": course.id,
            "status": course.status,
            "reservation_time": course.reservation_time,
            "tourist_id": course.tourist_id,
            "title": course.title,
            "created_at": course.created_at,
            "tour_list": tour_list,
        }

        courses_with_tour_list.append(course_data)

    return courses_with_tour_list




def get_courses_detail(db: Session, id: int = None):
    query = db.query(Course)


    if id:
        print("i got an id filter")
        query = query.filter(Course.id == id)


    courses = query.all()

    if not courses:
        return []  
    course_ids = [course.id for course in courses]
    attraction_ids = db.query(CourseAttractions.attraction_id).filter(CourseAttractions.course_id.in_(course_ids)).all()

    if not attraction_ids:
        return []  

    attraction_ids = [attraction_id for (attraction_id,) in attraction_ids]

    attractions = db.query(Attractions).filter(Attractions.id.in_(attraction_ids)).all()

    courses_with_tour_list = []
    for course in courses:
        tour_list = []

        for attraction in attractions:
            if attraction.id in attraction_ids:
                tour_list.append({
                    "attraction_id": attraction.id,
                    "name": attraction.name,
                    "description": attraction.description,
                    "latitude": attraction.latitude,
                    "longitude": attraction.longitude,
                })

        course_data = {
            "category": course.category,
            "id": course.id,
            "status": course.status,
            "reservation_time": course.reservation_time,
            "tourist_id": course.tourist_id,
            "title": course.title,
            "created_at": course.created_at,
            "tour_list": tour_list,
        }

        courses_with_tour_list.append(course_data)

    return courses_with_tour_list

def get_course_details(db: Session, course_id: int):
    courses = db.query(Course).filter(Course.id == course_id).all()
    

    if not courses:
        return []


    course_ids = [course.id for course in courses]
    attraction_ids = db.query(CourseAttractions.attraction_id).filter(CourseAttractions.course_id.in_(course_ids)).all()
    
    attraction_ids = [attraction_id for (attraction_id,) in attraction_ids]

    attractions = db.query(Attractions).filter(Attractions.id.in_(attraction_ids)).all()

    courses_with_detail = []

    for course in courses:

        course_attractions = [attraction for attraction in attractions if attraction.id in attraction_ids]

        course_data = {
            "category": course.category,
            "id": course.id,
            "status": course.status,
            "reservation_time": course.reservation_time,
            "tourist_id": course.tourist_id,
            "title": course.title,
            "created_at": course.created_at,
            "tour_list": [
                {
                    "attraction_id": attraction.id,
                    "name": attraction.name,
                    "description": attraction.description,
                    "latitude": attraction.latitude,
                    "longitude": attraction.longitude,
                }
                for attraction in course_attractions
            ],
        }

        courses_with_detail.append(course_data)

    return courses_with_detail



def get_my_course_list(db: Session, tourist_id: int):
    courses = db.query(Course).filter(Course.tourist_id == tourist_id).all()

    return courses



def create_course(db: Session, course_info: CreateCourse):
    
    course = Course(
        tourist_id=course_info.tourist_id,
        title=course_info.title,
        category=course_info.category,
        reservation_time=course_info.reservation_time,
    )
    db.add(course)
    db.commit()

    db.refresh(course)

    for attraction_info in course_info.attractions_list:
        course_attraction = CourseAttractions(
            course_id=course.id,
            attraction_id=attraction_info.attraction_id,
            order_num=attraction_info.order_num,
            is_last=attraction_info.is_last,
            departure_time=attraction_info.departure_time,
        )
        db.add(course_attraction)

    db.commit()
    return course.id


## course cost 
### get course id filter by tourist id
### get all data from course cost table filter by course id and order by cost 

def get_course_costs(db: Session, tourist_id: int):
    # Step 1: Get the most recently created course for the specified tourist ID
    recent_course = db.query(Course).filter(Course.tourist_id == tourist_id).order_by(desc(Course.created_at)).first()

    if not recent_course:
        return None

   # Step 2: Get the course cost data for the recent course and sort by cost in ascending order
    course_costs = (
        db.query(CourseCost)
        .filter(CourseCost.course_id == recent_course.id)
        .order_by(CourseCost.cost.asc())
        .all()
    )

    # Step 3: Return the recent course with its associated course costs
    course_data = {
        "course_id": recent_course.id,
        "title": recent_course.title,
        "category": recent_course.category,
        "reservation_time": recent_course.reservation_time,
        "course_costs": [
            {
                "cost": cost.cost,
                "driver_username": db.query(User.username).filter(User.id == cost.driver_id).first().username
            }
            for cost in course_costs
        ]
    }

    return course_data


def execute_trade(db: Session, tourist_id: int):
    recent_course = db.query(Course).filter(Course.tourist_id == tourist_id).order_by(desc(Course.created_at)).first()


    if not recent_course:
        return {"success": False, "message": "No recent course found for the specified tourist."}

    if recent_course.status == "TRADE_COMPLETED":
        return {"success": False, "message": "거래가 이미 완료된 코스입니다."}
    
    recent_course.status = "TRADE_COMPLETED"

    course_cost = (
        db.query(CourseCost)
        .filter(CourseCost.course_id == recent_course.id)
        .order_by(CourseCost.cost.asc())
        .first()
    )

    
    if course_cost:
        course_cost.is_selected = True
        db.commit()
        return {
            "success": True,
            "message": "Course cost selection updated successfully.",
            "course_data": {
                "course_id": recent_course.id,
                "title": recent_course.title,
                "category": recent_course.category,
                "reservation_time": recent_course.reservation_time,
                "course_cost": {
                    "cost": course_cost.cost,
                    "is_selected": course_cost.is_selected,
                    "driver_username": db.query(User.username).filter(User.id == course_cost.driver_id).first().username
                }
            }
        }
    else:
        return {"success": False, "message": "No course cost found for the recent course."}