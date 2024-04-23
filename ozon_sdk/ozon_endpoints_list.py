from .response import *
from .response import BaseResponse
from typing import Type
from .ozon_async_api import OzonAsyncApi
from .core import OzonAsyncEngine


class OzonAPIFactory:

    api_list: dict[Type[BaseResponse], str] = {
        PostingFBOListResponse: '/v2/posting/fbo/list',
        PostingFBSActCreateResponse: '/v2/posting/fbs/act/create',
        PostingCarriageAvailableListResponse: '/v1/posting/carriage-available/list',
        CarriageGetResponse: '/v1/carriage/get',
        PostingFBSActGetResponse: '/v2/posting/fbs/act/get-postings',
        FinanceTransactionListResponse: '/v3/finance/transaction/list',
        PostingFBSGetResponse: '/v3/posting/fbs/get',
        PostingFBOGetResponse: '/v2/posting/fbo/get'
    }

    def __init__(self, engine: OzonAsyncEngine):
        self._engine = engine

    def get_api(self, response_type: Type[BaseResponse]):
        url = OzonAPIFactory.api_list.get(response_type)
        api = OzonAsyncApi(self._engine, url, response_type)

        return api
