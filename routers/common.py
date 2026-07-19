from typing import NoReturn

from fastapi import HTTPException, status


def not_implemented() -> NoReturn:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Route is defined but its service is not implemented yet",
    )

