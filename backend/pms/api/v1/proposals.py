from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pms.api.deps import get_db
from pms.schemas.proposals import ProposalCreate
from pms.security.rbac import require_role
from pms.db import models
from sqlalchemy import func
from geoalchemy2.shape import from_shape
from shapely.geometry import shape

router = APIRouter(prefix="/proposals", tags=["proposals"])

@router.post("/", dependencies=[Depends(require_role("submitter"))])
def create_proposal(payload: ProposalCreate, db: Session = Depends(get_db)):
    geom_wkb = from_shape(shape(payload.geometry.model_dump()), srid=4326)
    p = models.Proposal(
        title=payload.title,
        pest_type=payload.pest_type,
        chemical=payload.chemical,
        rate=payload.rate,
        method=payload.method,
        geometry=geom_wkb,
        metadata=payload.metadata,
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    return {"id": p.id}

@router.get("/stats")
def proposal_stats(db: Session = Depends(get_db)):
    total = db.query(func.count(models.Proposal.id)).scalar()
    return {"total": total}
