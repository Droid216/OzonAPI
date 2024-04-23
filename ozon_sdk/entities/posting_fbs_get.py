from .picking import Picking
from .services import Services
from .base import BaseEntity
from datetime import datetime
from typing import Optional


class PostingFBSGetAdditionalData(BaseEntity):
    key: str = None
    value: str = None


class PostingFBSGetAddressee(BaseEntity):
    name: str = None
    phone: str = None


class PostingFBSGetAnalyticsData(BaseEntity):
    city: str = None
    delivery_date_begin: datetime = None
    delivery_date_end: datetime = None
    delivery_type: str = None
    is_legal: bool = None
    is_premium: bool = None
    payment_type_group_name: str = None
    region: str = None
    tpl_provider: str = None
    tpl_provider_id: int = None
    warehouse: str = None
    warehouse_id: int = None


class PostingFBSGetBarcodes(BaseEntity):
    lower_barcode: str = None
    upper_barcode: str = None


class PostingFBSGetCancellation(BaseEntity):
    affect_cancellation_rating: bool = None
    cancel_reason: str = None
    cancel_reason_id: int = None
    cancellation_initiator: str = None
    cancellation_type: str = None
    cancelled_after_ship: bool = None


class PostingFBSGetCourier(BaseEntity):
    car_model: str = None
    car_number: str = None
    name: str = None
    phone: str = None


class PostingFBSGetCustomerAddress(BaseEntity):
    address_tail: str = None
    city: str = None
    comment: str = None
    country: str = None
    district: str = None
    latitude: float = None
    longitude: float = None
    provider_pvz_code: str = None
    pvz_code: int = None
    region: str = None
    zip_code: str = None


class PostingFBSGetCustomer(BaseEntity):
    address: Optional[PostingFBSGetCustomerAddress] = None
    customer_email: str = None
    customer_id: int = None
    name: str = None
    phone: str = None


class PostingFBSGetDeliveryMethod(BaseEntity):
    id: int = None
    name: str = None
    tpl_provider: str = None
    tpl_provider_id: int = None
    warehouse: str = None
    warehouse_id: int = None


class PostingFBSGetFinancialDataProducts(BaseEntity):
    actions: list[str] = []
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


class PostingFBSGetFinancialData(BaseEntity):
    cluster_from: str = None
    cluster_to: str = None
    posting_services: Optional[Services] = None
    products: list[PostingFBSGetFinancialDataProducts] = []


class PostingFBSGetProductExemplarsProductsExemplars(BaseEntity):
    exemplar_id: int = None
    mandatory_mark: str = None
    gtd: str = None
    is_gtd_absent: bool = None
    rnpt: str = None
    is_rnpt_absent: bool = None


class PostingFBSGetProductExemplarsProducts(BaseEntity):
    exemplars: list[PostingFBSGetProductExemplarsProductsExemplars] = []
    sku: int = None


class PostingFBSGetProductExemplars(BaseEntity):
    products: list[PostingFBSGetProductExemplarsProducts] = []


class PostingFBSGetProductsDimensions(BaseEntity):
    height: str = None
    length: str = None
    weight: str = None
    width: str = None


class PostingFBSGetProducts(BaseEntity):
    dimensions: Optional[PostingFBSGetProductsDimensions] = None
    mandatory_mark: list[str] = []
    name: str = None
    offer_id: str = None
    price: str = None
    jw_uin: list[str] = None
    currency_code: str = None
    quantity: int = None
    sku: int = None


class PostingFBSGetPRROption(BaseEntity):
    code: str = None
    price: str = None
    currency_code: str = None
    floor: str = None


class PostingFBSGetRelatedPostings(BaseEntity):
    related_posting_numbers: list[str] = None


class PostingFBSGeRequirements(BaseEntity):
    products_requiring_gtd: list[int] = []
    products_requiring_country: list[int] = []
    products_requiring_mandatory_mark: list[int] = []
    products_requiring_jw_uin: list[int] = []
    products_requiring_rnpt: list[int] = []


class PostingFBSGet(BaseEntity):
    additional_data: list[PostingFBSGetAdditionalData] = []
    addressee: Optional[PostingFBSGetAddressee] = None
    analytics_data: Optional[PostingFBSGetAnalyticsData] = None
    barcodes: Optional[PostingFBSGetBarcodes] = None
    cancellation: Optional[PostingFBSGetCancellation] = None
    courier: Optional[PostingFBSGetCourier] = None
    customer: Optional[PostingFBSGetCustomer] = None
    delivering_date: datetime = None
    delivery_method: Optional[PostingFBSGetDeliveryMethod] = None
    delivery_price: str
    financial_data: Optional[PostingFBSGetFinancialData] = None
    in_process_at: datetime = None
    is_express: bool = None
    is_multibox: bool = None
    multi_box_qty: int = None
    order_id: int = None
    order_number: str = None
    parent_posting_number: str = None
    posting_number: str = None
    product_exemplars: Optional[PostingFBSGetProductExemplars] = None
    products: list[PostingFBSGetProducts] = []
    provider_status: str = None
    prr_option: Optional[PostingFBSGetPRROption] = None
    related_postings: Optional[PostingFBSGetRelatedPostings] = None
    requirements: Optional[PostingFBSGeRequirements] = None
    shipment_date: datetime = None
    status: str = None
    substatus: str = None
    tpl_integration_type: str = None
    tracking_number:  str = None
