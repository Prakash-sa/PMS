from pydantic import BaseModel
from .common import Geometry

class ProposalCreate(BaseModel):
    title: str
    pest_type: str
    chemical: str
    rate: str | None = None
    method: str | None = None
    geometry: Geometry
    metadata: dict | None = None

class ProposalOut(BaseModel):
    id: int
    title: str
    pest_type: str
    chemical: str
