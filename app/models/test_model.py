from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)