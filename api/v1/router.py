from fastapi import APIRouter
from api.v1.routes.books import router as books_router

router = APIRouter()

router.include_router(books_router, prefix="/books", tags=["books"])