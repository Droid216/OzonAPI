from datetime import datetime

from pydantic import validator
from .base import BaseRequest
from rfc3339_validator import validate_rfc3339


class FBSActCreateRequest(BaseRequest):
    containers_count: int = None
    delivery_method_id: int
    departure_date: datetime

    @validator('departure_date')
    def validate_departure_date(cls, v):
        if not validate_rfc3339(v):
            raise ValueError("date_start must be rfc3339 valid")
        return v

