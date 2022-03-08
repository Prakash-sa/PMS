from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pms.api.deps import get_db
from pms.services.geospatial import proposals_in_bbox

router = APIRouter(prefix="/maps", tags=["maps"])

@router.get("/bbox")
def bbox(minx: float, miny: float, maxx: float, maxy: float, db: Session = Depends(get_db)):
    return proposals_in_bbox(db, minx, miny, maxx, maxy)
