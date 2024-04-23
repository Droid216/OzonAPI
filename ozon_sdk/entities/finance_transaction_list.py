from .base import BaseEntity
from datetime import datetime
from typing import Optional


class FinanceTransactionListOperationsItems(BaseEntity):
    name: str = None
    sku: int = None


class FinanceTransactionListOperationsPosting(BaseEntity):
    delivery_schema: str = None
    order_date: str = None
    posting_number: str = None
    warehouse_id: int = None


class FinanceTransactionListOperationsServices(BaseEntity):
    name: str = None
    price: float = None


class FinanceTransactionListOperations(BaseEntity):
    accruals_for_sale: float = None
    amount: float = None
    delivery_charge: float = None
    items: list[FinanceTransactionListOperationsItems] = []
    operation_date: datetime = None
    operation_id: int = None
    operation_type: str = None
    operation_type_name: str = None
    posting: Optional[FinanceTransactionListOperationsPosting] = None
    return_delivery_charge: float = None
    sale_commission: float = None
    services: list[FinanceTransactionListOperationsServices] = None
    type: str = None


class FinanceTransactionList(BaseEntity):
    operations: list[FinanceTransactionListOperations] = []
    page_count: int = None
    row_count: int = None
