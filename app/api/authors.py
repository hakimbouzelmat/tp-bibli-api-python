from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.author_schema import AuthorCreate, AuthorResponse
from app.services.author_service import create_author, get_all_authors

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(" / ", response_model=AuthorResponse)
def create(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)

@router.get(" / ", response_model=list[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return get_all_authors(db)
