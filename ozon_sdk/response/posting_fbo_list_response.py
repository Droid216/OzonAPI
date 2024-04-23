from .base import BaseResponse
from ..entities import PostingFBOList


class PostingFBOListResponse(BaseResponse):
    result: list[PostingFBOList] = []
