from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.domain.books import book_schema, book_repository
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=book_schema.Book)
def create_book(book: book_schema.BookCreate, db: Session = Depends(get_db)):
    return book_repository.create_book(db=db, book=book)

@router.get("/{book_id}", response_model=book_schema.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = book_repository.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book