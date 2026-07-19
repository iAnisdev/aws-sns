from uuid import UUID

from fastapi import APIRouter, Response, status

from routers.common import not_implemented
from schemas.subscriptions import SubscriptionCreate, SubscriptionResponse


router = APIRouter(
    prefix="/apps/{app_id}/topics/{topic_id}/subscriptions",
    tags=["Subscriptions"],
)


@router.post("", response_model=SubscriptionResponse, status_code=status.HTTP_201_CREATED)
def create_subscription(
    app_id: UUID,
    topic_id: UUID,
    _: SubscriptionCreate,
) -> SubscriptionResponse:
    return not_implemented()


@router.get("", response_model=list[SubscriptionResponse])
def list_subscriptions(app_id: UUID, topic_id: UUID) -> list[SubscriptionResponse]:
    return not_implemented()


@router.get("/{subscription_id}", response_model=SubscriptionResponse)
def get_subscription(
    app_id: UUID,
    topic_id: UUID,
    subscription_id: UUID,
) -> SubscriptionResponse:
    return not_implemented()


@router.delete("/{subscription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_subscription(
    app_id: UUID,
    topic_id: UUID,
    subscription_id: UUID,
) -> Response:
    return not_implemented()

