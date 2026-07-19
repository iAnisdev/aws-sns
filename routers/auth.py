import os
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import jwt
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database.connection import get_db
from models.token import AuthToken
from schemas.auth import TokenPurpose, TokenRequest, TokenResponse


router = APIRouter(prefix="/auth", tags=["Authentication"])

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
COOKIE_SECURE = os.environ["COOKIE_SECURE"].lower() in {"1", "true", "yes", "on"}

TOKEN_EXPIRE_HOURS = {
    TokenPurpose.GENERAL: int(os.environ["GENERAL_TOKEN_EXPIRE_HOURS"]),
    TokenPurpose.ADMIN: int(os.environ["ADMIN_TOKEN_EXPIRE_HOURS"]),
    TokenPurpose.LOGS: int(os.environ["LOGS_TOKEN_EXPIRE_HOURS"]),
}


@router.post(
    "/token",
    response_model=TokenResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_token(
    request: TokenRequest,
    response: Response,
    db: Session = Depends(get_db),
) -> TokenResponse:
    session_id = str(uuid4())
    now = datetime.now(timezone.utc)
    expire_hours = TOKEN_EXPIRE_HOURS[request.purpose]
    expired_at = now + timedelta(hours=expire_hours)

    token = jwt.encode(
        {
            "sid": session_id,
            "purpose": request.purpose.value,
            "iat": now,
            "exp": expired_at,
        },
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )

    token_record = AuthToken(
        session_id=session_id,
        purpose=request.purpose.value,
        created_at=now.replace(tzinfo=None),
        expired_at=expired_at.replace(tzinfo=None),
        is_valid=True,
    )

    try:
        db.add(token_record)
        db.commit()
    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Could not create token session",
        ) from exc

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=COOKIE_SECURE,
        samesite="lax",
        max_age=expire_hours * 60 * 60,
    )

    return TokenResponse(session_id=session_id)
