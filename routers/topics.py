from uuid import UUID

from fastapi import APIRouter, Response, status

from routers.common import not_implemented
from schemas.topics import PublishMessageRequest, PublishMessageResponse, TopicCreate, TopicResponse


router = APIRouter(prefix="/apps/{app_id}/topics", tags=["Topics"])


@router.post("", response_model=TopicResponse, status_code=status.HTTP_201_CREATED)
def create_topic(app_id: UUID, _: TopicCreate) -> TopicResponse:
    return not_implemented()


@router.get("", response_model=list[TopicResponse])
def list_topics(app_id: UUID) -> list[TopicResponse]:
    return not_implemented()


@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(app_id: UUID, topic_id: UUID) -> TopicResponse:
    return not_implemented()


@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_topic(app_id: UUID, topic_id: UUID) -> Response:
    return not_implemented()


@router.post("/{topic_id}/messages", response_model=PublishMessageResponse)
def publish_message(
    app_id: UUID,
    topic_id: UUID,
    _: PublishMessageRequest,
) -> PublishMessageResponse:
    return not_implemented()

