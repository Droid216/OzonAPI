from .base import BaseResponse
from ..entities import PostingFBOGet


class PostingFBOGetResponse(BaseResponse):
    result: PostingFBOGet
