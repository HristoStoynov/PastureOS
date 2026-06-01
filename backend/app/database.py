from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/pastureos.db")

engine = create_engine(DATABASE_URL, echo=False)


def init_db():
    # create directories
    p = Path("./data")
    p.mkdir(parents=True, exist_ok=True)
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
