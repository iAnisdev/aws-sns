from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TopicCreate(BaseModel):
    name: str = Field(min_length=1, max_length=256)


class TopicResponse(BaseModel):
    topic_id: UUID
    app_id: UUID
    name: str
    arn: str | None = None
    created_at: datetime


class PublishMessageRequest(BaseModel):
    message: str = Field(min_length=1)
    subject: str | None = Field(default=None, max_length=100)
    attributes: dict[str, str] = Field(default_factory=dict)


class PublishMessageResponse(BaseModel):
    message_id: str

