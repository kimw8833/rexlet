from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rexlet.models import Base

DATABASE_URL = "sqlite:///rexlet.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)