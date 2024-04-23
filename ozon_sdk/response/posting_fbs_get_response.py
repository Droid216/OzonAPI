from .base import BaseResponse
from ..entities import PostingFBSGet


class PostingFBSGetResponse(BaseResponse):
    result: PostingFBSGet
