from .base import BaseEntity
from datetime import datetime
from typing import Optional
from .picking import Picking
from .services import Services


class AdditionalData(BaseEntity):
    key: str = None
    value: str = None


class PostingFBOListAnalyticsData(BaseEntity):
    city: str = None
    delivery_type: str = None
    is_legal: bool = None
    is_premium: bool = None
    payment_type_group_name: str = None
    region: str = None
    warehouse_id: int = None
    warehouse_name: str = None


class PostingFBOListFinancialDataProducts(BaseEntity):
    actions: list[str] = None
    currency_code: str = None
    commission_amount: float = None
    commission_percent: float = None
    commissions_currency_code: str = None
    item_services: Optional[Services] = None
    old_price: float = None
    payout: float = None
    picking: Optional[Picking] = None
    price: float = None
    product_id: int = None
    quantity: int = None
    total_discount_percent: float = None
    total_discount_value: float = None


class PostingFBOListFinancialData(BaseEntity):
    posting_services: Optional[Services] = None
    cluster_from: str = None
    cluster_to: str = None
    products: list[PostingFBOListFinancialDataProducts] = []


class FboPostingListProduct(BaseEntity):
    digital_code: str = None
    name: str = None
    offer_id: str = None
    price: str = None
    quantity: int = None
    sku: int = None


class PostingFBOList(BaseEntity):
    additional_data: list[AdditionalData] = []
    analytics_data: Optional[PostingFBOListAnalyticsData] = None
    cancel_reason_id: int = None
    created_at: datetime = None
    financial_data: Optional[PostingFBOListFinancialData] = None
    in_process_at: str = None
    order_id: int = None
    order_number: str = None
    posting_number: str = None
    products: list[FboPostingListProduct] = []
    status: str = None
