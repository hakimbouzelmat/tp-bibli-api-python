from sqlalchemy.orm import Session
from app.domain.books.book_model import Book

def get_book_by_isbn(db: Session, isbn: str):
    return db.query(Book).filter(Book.isbn == isbn).first()
