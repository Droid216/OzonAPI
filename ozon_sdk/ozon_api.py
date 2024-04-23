from .requests import *
from .response import *
from .core import OzonAsyncEngine
from .ozon_endpoints_list import OzonAPIFactory


class OzonApi:

    def __init__(self, client_id: str, api_key: str):
        self._engine = OzonAsyncEngine(client_id=client_id, api_key=api_key)
        self._api_factory = OzonAPIFactory(self._engine)

        self._posting_fbo_list_api = self._api_factory.get_api(PostingFBOListResponse)
        self._fbs_act_create_api = self._api_factory.get_api(PostingFBSActCreateResponse)
        self._posting_carriage_available_list_api = self._api_factory.get_api(PostingCarriageAvailableListResponse)
        self._posting_carriage_get_api = self._api_factory.get_api(CarriageGetResponse)
        self._posting_fbs_act_get_postings_api = self._api_factory.get_api(PostingFBSActGetResponse)
        self._finance_transaction_list_api = self._api_factory.get_api(FinanceTransactionListResponse)
        self._posting_fbs_get_api = self._api_factory.get_api(PostingFBSGetResponse)
        self._posting_fbo_get_api = self._api_factory.get_api(PostingFBOGetResponse)

    async def get_posting_fbo_list(self, dir: str, since: str, status: str, to: str, limit: int = 1000, offset: int = 0,
                                   translit: bool = True, analytics_data=False, financial_data=False) \
            -> PostingFBOListResponse:
        """_summary_

        Args:
            dir (str): Направление сортировки:
                asc — по возрастанию,
                desc — по убыванию.
            since (str): Начало периода в формате YYYY-MM-DD.
            status (str): Статус отправления.
                awaiting_packaging — ожидает упаковки,
                awaiting_deliver — ожидает отгрузки,
                delivering — доставляется,
                delivered — доставлено,
                cancelled — отменено.
            to (str): Конец периода в формате YYYY-MM-DD.
            limit (int, optional): Количество значений в ответе:
                максимум — 1000,
                минимум — 1.. Defaults to 1000.
            offset (int, optional): Количество элементов, которое будет пропущено в ответе. Например, если offset = 10, то ответ начнётся с 11-го найденного элемента.. Defaults to 0.
            translit (bool, optional): Если включена транслитерация адреса из кириллицы в латиницу — true.. Defaults to True.
            analytics_data (bool, optional): Передайте true, чтобы добавить в ответ данные аналитики.. Defaults to False.
            financial_data (bool, optional): Передайте true, чтобы добавить в ответ финансовые данные.. Defaults to False.
        """
        request = PostingFBOListRequest(dir=dir,
                                        filter=PostingFBOListFilter(since=since, status=status, to=to),
                                        limit=limit,
                                        offset=offset,
                                        translit=translit,
                                        with_field=PostingFBOListWith(analytics_data=analytics_data,
                                                                      financial_data=financial_data))
        answer: PostingFBOListResponse = await self._posting_fbo_list_api.post(request)

        return answer

    async def get_posting_fbs_act_create(self, delivery_method_id: int, departure_date: str,
                                         containers_count: int = None) -> PostingFBSActCreateResponse:
        """_summary_

        Args:
            delivery_method_id (int): Идентификатор метода доставки.
            departure_date (str): Дата отгрузки в формате YYYY-MM-DD.
            containers_count (int, optional): Количество грузовых мест.
                Используйте параметр, если вы подключены к доверительной приёмке и отгружаете заказы грузовыми местами.
                Если вы не подключены к доверительной приёмке, пропустите его.
        """
        request = FBSActCreateRequest(containers_count=containers_count,
                                      delivery_method_id=delivery_method_id,
                                      departure_date=departure_date)
        answer: PostingFBSActCreateResponse = await self._fbs_act_create_api.post(request)

        return answer

    async def get_posting_carriage_available_list(self, delivery_method_id: int,
                                                  departure_date: str = datetime.now().astimezone().isoformat()) \
            -> PostingCarriageAvailableListResponse:
        """_summary_

        Args:
            delivery_method_id (int): Фильтр по методу доставки.
            departure_date (str, optional): Дата отгрузки в формате YYYY-MM-DD.. Defaults to текущая дата.
        """
        request = PostingCarriageAvailableListRequest(delivery_method_id=delivery_method_id,
                                                      departure_date=departure_date)
        answer: PostingCarriageAvailableListResponse = await self._posting_carriage_available_list_api.post(request)

        return answer

    async def get_carriage(self, carriage_id: int) -> CarriageGetResponse:
        """_summary_

        Args:
            carriage_id (int): Идентификатор перевозки.
        """
        request = CarriageGetRequest(carriage_id=carriage_id)
        answer: CarriageGetResponse = await self._posting_carriage_available_list_api.post(request)

        return answer

    async def get_posting_fbs_act_postings(self, act_id: int) -> PostingFBSActGetResponse:
        """_summary_

        Args:
            act_id (int): Идентификатор акта.
        """
        request = PostingFBSActGetPostingsRequest(id=act_id)
        answer: PostingFBSActGetResponse = await self._posting_fbs_act_get_postings_api.post(request)

        return answer

    async def get_finance_transaction_list(self, from_field: str, to: str, posting_number: str = "",
                                           operation_type: list[str] = None, transaction_type: str = 'all', page: int = 1,
                                           page_size: int = 1000) -> FinanceTransactionListResponse:
        """_summary_

        Args:
            from_field (str): Начало периода в формате YYYY-MM-DD.
            to (str): Конец периода в формате YYYY-MM-DD.
            posting_number (str, optional): Номер отправления.
            operation_type (bool, optional):
            transaction_type (str, optional): Тип начисления(некоторые операции могут быть разделены во времени):
                all — все,
                orders — заказы,
                returns — возвраты и отмены,
                services — сервисные сборы,
                compensation — компенсация,
                transferDelivery — стоимость доставки,
                other — прочее.. Defaults to all.
            page (int, optional): Номер страницы, возвращаемой в запросе.. Defaults to 1.
            page_size (int, optional): Количество элементов на странице.. Defaults to 1000
        """
        if operation_type is None:
            operation_type = []
        request = FinanceTransactionListRequest(filter=FinanceTransactionListFilter(date=FinanceTransactionListDate(from_field=from_field,
                                                                                                                    to=to),
                                                                                    operation_type=operation_type,
                                                                                    posting_number=posting_number,
                                                                                    transaction_type=transaction_type),
                                                page=page,
                                                page_size=page_size)
        answer: FinanceTransactionListResponse = await self._finance_transaction_list_api.post(request)

        return answer

    async def get_posting_fbs(self, posting_number: str, analytics_data: bool = False, barcodes: bool = False,
                              financial_data: bool = False, product_exemplars: bool = False,
                              related_postings: bool = False, translit: bool = False) -> PostingFBSGetResponse:
        """_summary_

        Args:
            posting_number (str, optional): Номер отправления.
            analytics_data (bool, optional): Добавить в ответ данные аналитики.. Defaults to False.
            barcodes (bool, optional): Добавить в ответ штрихкоды отправления.. Defaults to False.
            financial_data (bool, optional): Добавить в ответ финансовые данные.. Defaults to False.
            product_exemplars (bool, optional): Добавить в ответ данные о продуктах и их экземплярах.. Defaults to False.
            related_postings (bool, optional): Добавить в ответ номера связанных отправлений.
                Связанные отправления — те, на которое было разделено родительское отправление при сборке..
                Defaults to False.
            translit (bool, optional): Выполнить транслитерацию возвращаемых значений.. Defaults to False.
        """
        request = PostingFBSGetRequest(posting_number=posting_number,
                                       with_field=PostingFBSGetWith(analytics_data=analytics_data,
                                                                    barcodes=barcodes,
                                                                    financial_data=financial_data,
                                                                    product_exemplars=product_exemplars,
                                                                    related_postings=related_postings,
                                                                    translit=translit))
        answer: PostingFBSGetResponse = await self._posting_fbs_get_api.post(request)
        return answer

    async def get_posting_fbo(self, posting_number: str, analytics_data: bool = False, financial_data: bool = False,
                              translit: bool = False) -> PostingFBOGetResponse:
        """_summary_

        Args:
            posting_number (str, optional): Номер отправления.
            analytics_data (bool, optional): Добавить в ответ данные аналитики.. Defaults to False.
            financial_data (bool, optional): Добавить в ответ финансовые данные.. Defaults to False.
            translit (bool, optional): Выполнить транслитерацию возвращаемых значений.. Defaults to False.
        """
        request = PostingFBOGetRequest(posting_number=posting_number,
                                       translit=translit,
                                       with_field=PostingFBOGetWith(analytics_data=analytics_data,
                                                                    financial_data=financial_data))
        answer: PostingFBOGetResponse = await self._posting_fbo_get_api.post(request)
        return answer
