from fastapi import APIRouter
from pms.services.recommendations import recommend_best_practices

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.post("/")
def recommend(pest_type: str, context: dict = {}):
    return recommend_best_practices(pest_type, context)
