from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

DATABASE_URL = "postgresql+psycopg2://postgres:everythingtime@127.0.0.1:5434/nutrition_db"


engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))
    print("DATABASE CONNECTED")
