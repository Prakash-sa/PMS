from sqlalchemy import text
from sqlalchemy.orm import Session

def proposals_in_bbox(db: Session, minx: float, miny: float, maxx: float, maxy: float):
    q = text(
        '''
        SELECT id, title, pest_type, chemical
        FROM proposals
        WHERE ST_Intersects(
            geometry,
            ST_MakeEnvelope(:minx, :miny, :maxx, :maxy, 4326)
        )
        '''
    )
    return db.execute(q, {"minx": minx, "miny": miny, "maxx": maxx, "maxy": maxy}).mappings().all()
