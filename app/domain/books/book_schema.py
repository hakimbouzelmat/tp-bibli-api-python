from pydantic import BaseModel, Field, field_validator
from typing import Optional

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author_id: int

    isbn: str = Field(..., pattern=r"^[\d-]+$") 

    model_config = {"from_attributes": True}

    @field_validator("isbn")
    @classmethod
    def validate_isbn_length(cls, v: str):

        digits_only = v.replace("-", "")
        if len(digits_only) not in [10, 13]:
            raise ValueError("L'ISBN doit contenir 10 ou 13 chiffres.")
        return v

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author_id: Optional[int] = None
    isbn: Optional[str] = None

    model_config = {"from_attributes": True}

class Book(BookBase):
    id: int