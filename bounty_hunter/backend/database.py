from sqlalchemy import create_engine
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./galactic_bounty_board.db"

# check_same_thread must be disabled for SQLite with FastAPI requests.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

def get_db():
    with Session(engine) as db:
        yield db