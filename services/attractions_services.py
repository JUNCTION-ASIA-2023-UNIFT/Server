from sqlalchemy.orm import Session
from models.attractions_model import Attractions

def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Attractions).offset(skip).limit(limit).all()