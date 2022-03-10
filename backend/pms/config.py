from pydantic_settings import BaseSettings
from typing import List
import os


def _parse_cors(origins: str | None) -> List[str]:
    if not origins:
        return ["http://localhost:5173"]
    # Allow both JSON-style (['a','b']) or comma-separated strings
    origins = origins.strip()
    if origins.startswith("[") and origins.endswith("]"):
        # crude attempt to parse list-like string
        origins = origins.strip("[]")
    parts = [p.strip().strip('"').strip("'") for p in origins.split(",") if p.strip()]
    return parts if parts else ["http://localhost:5173"]


class Settings(BaseSettings):
    env: str = "development"
    database_url: str
    oidc_issuer_url: str | None = None
    oidc_audience: str | None = None
    oidc_client_id: str | None = None
    cors_origins: List[str] = []
    redis_url: str = "redis://redis:6379/0"
    REC_MODEL_PATH: str = os.getenv("REC_MODEL_PATH", "/app/pms_rec/artifacts/best_practices_pipeline.pkl")

    class Config:
        env_file = ".env"


# Build database_url from env vars if not provided explicitly
database_url = os.environ.get("DATABASE_URL")
if not database_url:
    database_url = (
        f"postgresql+psycopg://{os.environ.get('POSTGRES_USER','pms')}:"
        f"{os.environ.get('POSTGRES_PASSWORD','pms')}@"
        f"{os.environ.get('POSTGRES_HOST','db')}:"
        f"{os.environ.get('POSTGRES_PORT','5432')}/"
        f"{os.environ.get('POSTGRES_DB','pms')}"
    )

# Parse CORS origins from env var CORS_ORIGINS (comma separated or JSON list)
cors_env = os.environ.get("CORS_ORIGINS") or os.environ.get("cors_origins")
cors_list = _parse_cors(cors_env)

settings = Settings(database_url=database_url, cors_origins=cors_list)

