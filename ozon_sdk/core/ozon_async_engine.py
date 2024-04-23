import aiohttp


class OzonAsyncEngine:
    """_summary_
    """

    def __init__(self, client_id: str = '', api_key: str = ''):
        """_summary_

        Args:
            client_id (str, optional): _description_. Defaults to ''.
            api_key (str, optional): _description_. Defaults to ''.
        """
        self._base_url = 'https://api-seller.ozon.ru'
        self.__headers = {
            'Client-Id': client_id,
            'Api-Key': api_key
        }

    async def get(self, url: str, params: dict) -> dict:
        """_summary_

        Args:
            url (str): _description_
            params (dict): _description_

        Returns:
            dict: _description_
        """

        url = await self._get_url(url)
        response = await self._perform_get_request(url, params)

        return response

    async def post(self, url: str, params: dict) -> dict:
        """_summary_

        Args:
            url (str): _description_
            params (dict): _description_

        Returns:
            dict: _description_
        """
        url = await self._get_url(url)
        response = await self._perform_post_request(url, params)

        return response

    async def _get_url(self, url: str):
        """_summary_

        Args:
            url (_type_): _description_

        Returns:
            _type_: _description_
        """
        if url.startswith("/"):
            return self._base_url + url
        else:
            return f"{self._base_url}/{url}"

    async def _perform_get_request(self, url, params):
        """_summary_

        Args:
            url (_type_): _description_
            params (_type_): _description_

        Returns:
            _type_: _description_
        """
        async with await self._get_session() as session:
            async with session.get(url, params=params) as response:
                return await response.json(content_type=None)

    async def _perform_post_request(self, url, params):
        """_summary_

        Args:
            url (_type_): _description_
            params (_type_): _description_

        Returns:
            _type_: _description_
        """
        async with await self._get_session() as session:
            async with session.post(url, json=params) as response:
                return await response.json()

    async def _get_session(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        session = aiohttp.ClientSession()

        session.headers["Client-Id"] = self.__headers['Client-Id']
        session.headers["Api-Key"] = self.__headers['Api-Key']

        return session
