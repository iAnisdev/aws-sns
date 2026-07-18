import os
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import jwt
from fastapi import APIRouter, Response, status

from schemas.auth import TokenPurpose, TokenRequest, TokenResponse


router = APIRouter(prefix="/auth", tags=["Authentication"])

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
COOKIE_SECURE = os.environ["COOKIE_SECURE"].lower() in {"1", "true", "yes", "on"}

TOKEN_EXPIRE_HOURS = {
    TokenPurpose.GENERAL: int(os.environ["GENERAL_TOKEN_EXPIRE_HOURS"]),
    TokenPurpose.LOGS: int(os.environ["LOGS_TOKEN_EXPIRE_HOURS"]),
    TokenPurpose.OTHER: int(os.environ["OTHER_TOKEN_EXPIRE_HOURS"]),
}


@router.post(
    "/token",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_token(request: TokenRequest, response: Response) -> TokenResponse:
    session_id = str(uuid4())
    now = datetime.now(timezone.utc)
    expire_hours = TOKEN_EXPIRE_HOURS[request.purpose]

    token = jwt.encode(
        {
            "sid": session_id,
            "purpose": request.purpose.value,
            "iat": now,
            "exp": now + timedelta(hours=expire_hours),
        },
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite="lax",
        max_age=expire_hours * 60 * 60,
    )

    return TokenResponse(session_id=session_id)
