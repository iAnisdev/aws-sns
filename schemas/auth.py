from enum import Enum

from pydantic import BaseModel


class TokenPurpose(str, Enum):
    GENERAL = "general"
    ADMIN = "admin"
    LOGS = "logs"


class TokenRequest(BaseModel):
    purpose: TokenPurpose = TokenPurpose.GENERAL


class TokenResponse(BaseModel):
    session_id: str
