from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.books import router as books_router  
from app.api.authors import router as authors_router

app = FastAPI(
    title="Library API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(books_router) 

@app.get("/")
def root():
    return {"status": "Library API running"}

app.include_router(authors_router, prefix="/authors", tags=["Authors"])
