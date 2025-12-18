from fastapi import FastAPI
from app.api.books import router as books_router
from app.api.authors import router as authors_router
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bibliothèque API")

app.include_router(books_router, prefix="/books", tags=["Books"])
app.include_router(authors_router, prefix="/authors", tags=["Authors"])

@app.get("/")
def read_root():
    return {"message": "Wsh la street"}