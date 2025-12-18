from sqlalchemy.orm import Session
from app.domain.authors.author_model import Author
from app.schemas.author_schema import AuthorCreate


def create_author(db: Session, author: AuthorCreate) -> Author:
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_all_authors(db: Session):
    return db.query(Author).all()
