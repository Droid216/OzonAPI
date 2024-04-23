from .base import BaseRequest
from pydantic import Field


class PostingFBOGetWith(BaseRequest):
    analytics_data: bool
    financial_data: bool


class PostingFBOGetRequest(BaseRequest):
    posting_number: str
    translit: bool
    with_field: PostingFBOGetWith = Field(default=None, serialization_alias='with')
