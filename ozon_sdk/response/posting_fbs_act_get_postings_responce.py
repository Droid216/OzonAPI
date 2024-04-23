from .base import BaseResponse
from ..entities import PostingFBSActGet


class PostingFBSActGetResponse(BaseResponse):
    result: list[PostingFBSActGet] = []
