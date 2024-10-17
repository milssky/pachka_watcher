from http import HTTPMethod

from httpx import AsyncClient, Response

from pachka_watcher.integrations.auth import PachkaAuth
from pachka_watcher.settings import PachkaIntegrationSettings


class AsyncPachkaClient(AsyncClient):
    """Клиент для запросов в пачку."""
    def __init__(self, config: PachkaIntegrationSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.auth = PachkaAuth(config.access_token)

    async def get(self, url: str, **kwargs) -> Response:
        """Выполняет авторизованный GET запрос на заданный url."""
        response = await self.request(HTTPMethod.GET, url, auth=self.auth, **kwargs)
        response.raise_for_status()
        return response
    
    async def post(self, url: str, **kwargs) -> Response:
        """Выполняет авторизованный POST запрос на заданный url."""
        response = await self.request(HTTPMethod.POST, url, auth=self.auth, **kwargs)
        response.raise_for_status()
        return response
