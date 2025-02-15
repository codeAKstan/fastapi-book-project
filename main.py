from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.router import router as v1_router

from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)
app.include_router(v1_router, prefix="/api/v1")

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
