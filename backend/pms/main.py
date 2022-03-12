from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pms.config import settings
from pms.api.v1.router import router as api_v1

app = FastAPI(title="pms API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_v1, prefix="/api/v1")
