from datetime import datetime
from .base import BaseEntity


class PostingFBSActGetProducts(BaseEntity):
    name: str = None
    offer_id: str = None
    price: str = None
    quantity: int = None
    sku: int = None


class PostingFBSActGet(BaseEntity):
    id: int = None
    multi_box_qty: int = None
    posting_number: str = None
    status: str = None
    seller_error: str = None
    updated_at: datetime = None
    created_at: datetime = None
    products: list[PostingFBSActGetProducts] = []
