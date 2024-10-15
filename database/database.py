from config import db_url
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
engine = create_engine(db_url)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)