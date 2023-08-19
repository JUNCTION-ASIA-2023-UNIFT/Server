from fastapi import Depends, FastAPI, Body
from sqlalchemy.orm import Session

from models import attractions_model
from config.database import engine
from routers import attractions_routers

attractions_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(attractions_routers.router)

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}
