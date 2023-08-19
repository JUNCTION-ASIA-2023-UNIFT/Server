from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

# MySQL Database Configuration
DATABASE_HOST = os.getenv("MYSQL_HOST", "localhost")
DATABASE_PORT = int(os.getenv("MYSQL_PORT", "3306"))
DATABASE_USER = os.getenv("MYSQL_USER", "root")
DATABASE_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
DATABASE_NAME = os.getenv("MYSQL_DATABASE", "my_database")


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
