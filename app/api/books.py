from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.domain.books.book_model import Book
from app.domain.books.book_shema import BookCreate
from app.domain.books.book_repository import get_book_by_isbn
from app.domain.books.book_rules import can_delete_book

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    existing = get_book_by_isbn(db, book.isbn)
    if existing:
        raise HTTPException(
            status_code=400,
            detail="ISBN déjà existant"
        )

    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@router.get("/")
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Livre introuvable"
        )
    return book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(
            status_code=404,
            detail="Livre introuvable"
        )

    has_active_loans = False  
    if not can_delete_book(has_active_loans):
        raise HTTPException(
            status_code=400,
            detail="Livre avec emprunt actif"
        )

    db.delete(book)
