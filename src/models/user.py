from database.database import Base
from sqlalchemy import Column , Integer , String

class user(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True )
    name = Column(String)
    email = Column(String)
    password = Column(String)