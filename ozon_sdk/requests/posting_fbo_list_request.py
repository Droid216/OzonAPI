from pydantic import validator
from .base import BaseRequest
from pydantic import Field
from enum import Enum
from rfc3339_validator import validate_rfc3339


class StatusEnum(str, Enum):
    empty = ''
    awaiting_packaging = 'awaiting_packaging'
    awaiting_deliver = 'awaiting_deliver'
    delivering = 'delivering'
    delivered = 'delivered'
    cancelled = 'cancelled'


class PostingFBOListFilter(BaseRequest):
    since: str
    status: StatusEnum
    to: str

    @validator('since')
    def validate_since(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

    @validator('to')
    def validate_to(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v


class PostingFBOListWith(BaseRequest):
    analytics_data: bool
    financial_data: bool


class PostingFBOListRequest(BaseRequest):
    """Список отправлений"""
    dir: str
    filter: PostingFBOListFilter
    limit: int
    offset: int
    translit: bool
    with_field: PostingFBOListWith = Field(default=None, serialization_alias='with')

    @validator('limit')
    def validate_limit(cls, v):
        if v > 1000:
            return 1000
        if v < 1:
            return 1
        return v
