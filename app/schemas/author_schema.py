from pydantic import BaseModel, Field
from typing import Optional

class AuthorBase(BaseModel):
    name: str = Field(..., min_length=1)
    bio: Optional[str] = None

    model_config = {"from_attributes": True}

class AuthorCreate(AuthorBase):
    pass

class AuthorResponse(AuthorBase):
    id: int