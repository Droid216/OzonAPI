from .base import BaseEntity


class CarriageGetCancelAvailability(BaseEntity):
    is_cancel_available: bool = None
    reason: str = None
