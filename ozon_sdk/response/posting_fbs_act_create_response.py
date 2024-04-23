from .base import BaseResponse
from ..entities import PostingFBSActCreate


class PostingFBSActCreateResponse(BaseResponse):
    result: list[PostingFBSActCreate] = []
