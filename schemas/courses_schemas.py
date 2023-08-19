from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AttractionInfo(BaseModel):
    attraction_id: int
    order_num: int
    is_last: bool
    departure_time: datetime

class CreateCourse(BaseModel):
    tourist_id: int
    title: str
    category: str
    reservation_time: datetime
    attractions_list: List[AttractionInfo]