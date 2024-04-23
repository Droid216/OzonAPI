from .base import BaseResponse
from ..entities import PostingCarriageAvailableList


class PostingCarriageAvailableListResponse(BaseResponse):
    result: list[PostingCarriageAvailableList] = []
