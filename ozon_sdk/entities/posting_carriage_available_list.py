from .base import BaseEntity

from datetime import datetime
from typing import Optional


class PostingCarriageAvailableListErrors(BaseEntity):
    code: str = None
    status: str = None


class PostingCarriageAvailableList(BaseEntity):
    carriage_id: int = None
    carriage_postings_count: int = None
    carriage_status: str = None
    cutoff_at: datetime = None
    delivery_method_id: int = None
    delivery_method_name: str = None
    errors: Optional[PostingCarriageAvailableListErrors] = None
    first_mile_type: str = None
    has_entrusted_acceptance: bool = None
    mandatory_postings_count: int = None
    mandatory_packaged_count: int = None
    tpl_provider_icon_url: str = None
    tpl_provider_name: str = None
    warehouse_city: str = None
    warehouse_id: str = None
    warehouse_name: str = None
    warehouse_timezone: str = None
