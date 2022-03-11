from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, JSON, Boolean
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from pms.db.base import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    reviewer = "reviewer"
    submitter = "submitter"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    sub = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.submitter)
    is_active = Column(Boolean, default=True)

class Proposal(Base):
    __tablename__ = "proposals"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    pest_type = Column(String, nullable=False)
    chemical = Column(String, nullable=False)
    rate = Column(String, nullable=True)
    method = Column(String, nullable=True)
    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_by = relationship("User")
    geometry = Column(Geometry(geometry_type="MULTIPOLYGON", srid=4326), nullable=False)
    metadata = Column(JSON, nullable=True)

class ApprovalStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Approval(Base):
    __tablename__ = "approvals"
    id = Column(Integer, primary_key=True)
    proposal_id = Column(Integer, ForeignKey("proposals.id", ondelete="CASCADE"))
    status = Column(Enum(ApprovalStatus), default=ApprovalStatus.pending)
    reviewer_id = Column(Integer, ForeignKey("users.id"))
    reviewed_at = Column(DateTime)
    notes = Column(String)
    proposal = relationship("Proposal")
