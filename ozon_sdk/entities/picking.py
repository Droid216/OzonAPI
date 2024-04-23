from datetime import datetime

from .base import BaseEntity


class Picking(BaseEntity):
    amount: float
    moment: datetime
    tag: str
