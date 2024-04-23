from .base import BaseResponse
from ..entities import FinanceTransactionList


class FinanceTransactionListResponse(BaseResponse):
    result: FinanceTransactionList
