from .base import BaseRequest
from pydantic import Field


class PostingFBSGetWith(BaseRequest):
    analytics_data: bool
    barcodes: bool
    financial_data: bool
    product_exemplars: bool
    related_postings: bool
    translit: bool


class PostingFBSGetRequest(BaseRequest):
    posting_number: str
    with_field: PostingFBSGetWith = Field(default=None, serialization_alias='with')
