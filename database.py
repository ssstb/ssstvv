import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

raw_url = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@postgres_db:5432/postgres",
)
DATABASE_URL = raw_url.replace("postgresql://", "postgresql+psycopg2://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        