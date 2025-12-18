from sqlalchemy.orm import Session
from .book_model import Book as BookModel
from .book_schema import BookCreate

def get_book(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()

def create_book(db: Session, book: BookCreate):

    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book