from sqlalchemy import (
    Column, Integer, String, Text, Enum,
    ForeignKey, CheckConstraint
)
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.shared.enums import CategoryEnum

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    isbn = Column(String(13), unique=True, nullable=False)

    publication_year = Column(Integer, nullable=False)

    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)

    description = Column(Text)

    category = Column(Enum(CategoryEnum), nullable=False)

    language = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    publisher = Column(String, nullable=False)

    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    author = relationship("Author")

    __table_args__ = (
        CheckConstraint(
            "available_copies <= total_copies",
            name="check_copies"
        ),
    )
