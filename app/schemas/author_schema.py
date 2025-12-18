from datetime import date
from pydantic import BaseModel, Field

class AuthorBase(BaseModel):
    first_name: str = Field(..., example="Victor")
    last_name: str = Field(..., example="Hugo")
    birth_date: date
    nationality: str = Field(..., min_length=2, max_length=2)
    biography: str | None = None
    death_date: date | None = None

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int

    class Config:
        from_attributes = True
