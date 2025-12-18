# app/domain/books/book_schema.py

from pydantic import BaseModel, Field
from typing import Optional
from app.shared.enums import CategoryEnum


class BookBase(BaseModel):
    title: str = Field(..., min_length=1)
    isbn: str = Field(..., pattern=r"^\d{13}$")
    publication_year: int = Field(..., ge=1450)
    author_id: int
    total_copies: int = Field(..., ge=1)
    available_copies: int = Field(..., ge=0)
    description: Optional[str] = None
    category: CategoryEnum
    language: str
    pages: int = Field(..., ge=1)
    publisher: str


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True
