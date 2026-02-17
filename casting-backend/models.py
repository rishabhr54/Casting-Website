from pydantic import BaseModel

class CastingInput(BaseModel):
    length: float
    breadth: float
    height: float
    material: str

from fastapi import UploadFile
