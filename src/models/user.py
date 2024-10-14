from database.database import Base
from sqlalchemy import column , Integer , String

class user(Base):
    __tablename__="user"
    id = column(Integer,primary_key=true,index=true)
    name = column(String)
    amail = column(String)
    password = column(String)