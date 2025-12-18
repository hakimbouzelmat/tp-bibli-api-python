from sqlalchemy import Column, Integer, String, Date, Text
from app.core.database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    nationality = Column(String(2), nullable=False)
    biography = Column(Text, nullable=True)
    death_date = Column(Date, nullable=True)
