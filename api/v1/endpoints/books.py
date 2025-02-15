from fastapi import APIRouter, HTTPException
from api.db.schemas import books_db

router = APIRouter()

@router.get("/{book_id}")
def get_book(book_id: int):
    """Retrieve a book by its ID."""
    book = next((book for book in books_db if book["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book