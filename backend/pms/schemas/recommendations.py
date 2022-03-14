from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    pest_type: str
    context: dict = {}
