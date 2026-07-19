from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class AppCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class AppUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)


class AppResponse(BaseModel):
    app_id: UUID
    name: str
    created_at: datetime

