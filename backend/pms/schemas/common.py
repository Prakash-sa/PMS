from pydantic import BaseModel, Field

class Geometry(BaseModel):
    type: str = Field(default="MultiPolygon")
    coordinates: list
