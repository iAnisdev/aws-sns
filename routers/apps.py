from uuid import UUID

from fastapi import APIRouter, Response, status

from routers.common import not_implemented
from schemas.apps import AppCreate, AppResponse, AppUpdate


router = APIRouter(prefix="/apps", tags=["Apps"])


@router.post("", response_model=AppResponse, status_code=status.HTTP_201_CREATED)
def create_app(_: AppCreate) -> AppResponse:
    return not_implemented()


@router.get("", response_model=list[AppResponse])
def list_apps() -> list[AppResponse]:
    return not_implemented()


@router.get("/{app_id}", response_model=AppResponse)
def get_app(app_id: UUID) -> AppResponse:
    return not_implemented()


@router.patch("/{app_id}", response_model=AppResponse)
def update_app(app_id: UUID, _: AppUpdate) -> AppResponse:
    return not_implemented()


@router.delete("/{app_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_app(app_id: UUID) -> Response:
    return not_implemented()

