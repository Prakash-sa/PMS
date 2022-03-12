from pydantic import BaseModel

class ApprovalUpdate(BaseModel):
    status: str
    notes: str | None = None
