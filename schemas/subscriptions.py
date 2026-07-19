from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class SubscriptionProtocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"
    EMAIL = "email"
    EMAIL_JSON = "email-json"
    SQS = "sqs"
    LAMBDA = "lambda"
    SMS = "sms"


class SubscriptionCreate(BaseModel):
    protocol: SubscriptionProtocol
    endpoint: str
    filter_policy: dict[str, Any] | None = None


class SubscriptionResponse(BaseModel):
    subscription_id: UUID
    topic_id: UUID
    protocol: SubscriptionProtocol
    endpoint: str
    arn: str | None = None
    confirmed: bool
    created_at: datetime

