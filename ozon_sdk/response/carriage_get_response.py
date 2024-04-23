from datetime import datetime

from .base import BaseResponse
from ..entities import CarriageGetCancelAvailability
from typing import Optional


class CarriageGetResponse(BaseResponse):
    act_type: str = None
    arrival_pass_ids: list[str] = []
    cancel_availability: Optional[CarriageGetCancelAvailability] = None
    carriage_id: int = None
    company_id: int = None
    containers_count: int = None
    created_at: datetime = None
    delivery_method_id: int = None
    departure_date: str = None
    first_mile_type: str = None
    has_postings_for_next_carriage: bool = None
    integration_type: str = None
    is_container_label_printed: bool = None
    is_partial: bool = None
    partial_num: int = None
    retry_count: int = None
    status: str = None
    tpl_provider_id: int = None
    updated_at: datetime = None
    warehouse_id: int = None
