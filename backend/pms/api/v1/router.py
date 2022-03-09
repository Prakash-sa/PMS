from fastapi import APIRouter
from . import proposals, maps, recommendations

router = APIRouter()
router.include_router(proposals.router)
router.include_router(maps.router)
router.include_router(recommendations.router)
