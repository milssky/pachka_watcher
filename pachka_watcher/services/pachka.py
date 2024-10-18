from datetime import datetime, timedelta
from http import HTTPMethod
from json import JSONDecodeError
<<<<<<< HEAD
from typing import Sequence, Type, TypeVar
=======
from typing import Type, TypeVar
>>>>>>> 40ddd30a2222e07214cb285f275da7dff0b36a58

from httpx import AsyncClient, Response
from pydantic import BaseModel

from pachka_watcher.exceptions import JSONError
from pachka_watcher.integrations.client import AsyncPachkaClient
from pachka_watcher.schemas.messages import Message, Reaction

API_ROOT = "https://api.pachca.com/api/shared/v1"
MESSAGES_PER_PAGE = 50
Model = TypeVar("Model", bound=BaseModel)


class PachkaService:
    """Сервис для работы с Pachka."""

    def __init__(self, client: AsyncClient):
        self.client = client
        self.method_map = {
            HTTPMethod.GET: self.client.get,
            HTTPMethod.POST: self.client.post,
        }

    def _check_response(self, response: Response) -> Response:
        """Проверяет ответ на корректность."""
        try:
            response = response.json()
        except (JSONDecodeError, TypeError) as e:
            raise JSONError(f"Ошибка при обработке ответа: {e}")
        if "data" not in response:
            raise KeyError("Пустой ответ. Нет ключа data")
        return response

    async def _get_objects(
<<<<<<< HEAD
        self,
        url: str,
        cls: Type[Model],
        http_method: HTTPMethod = HTTPMethod.GET,
    ) -> Sequence[Model]:
        """Возвращает список объектов класса cls по url."""
        method = self.method_map.get(http_method)
        response = self._check_response(await method(url))
        return (cls(**obj) for obj in response["data"])

    async def get_chat_messages(self, chat_id: int) -> Sequence[Message]:
=======
        self, url: str, cls: Type[Model], method: HTTPMethod = HTTPMethod.GET
    ) -> list[Model]:
        if method == HTTPMethod.GET:
            response = await self.client.get(url)
        else:
            response = await self.client.post(url)
        response = self._check_response(response)
        return [cls(**obj) for obj in response["data"]]

    async def get_chat_messages(self, chat_id: int) -> list[Message]:
>>>>>>> 40ddd30a2222e07214cb285f275da7dff0b36a58
        """Возвращает список сообщений для конкретного чата."""
        url = f"{API_ROOT}/messages?chat_id={chat_id}&per={MESSAGES_PER_PAGE}"
        return await self._get_objects(url, Message)

<<<<<<< HEAD
    async def get_recent_messages(
        self, chat_id: int, hours: int = 60
    ) -> Sequence[Message]:
=======
    async def get_recent_messages(self, chat_id: int, hours: int = 60) -> list[Message]:
>>>>>>> 40ddd30a2222e07214cb285f275da7dff0b36a58
        """Возвращает список последних сообщений за hours для конкретного чата."""
        messages = await self.get_chat_messages(chat_id)
        last_messages = (
            message
            for message in messages
            if message.created_at.timestamp()
            >= (datetime.now() - timedelta(hours=hours)).timestamp()
            and message.content != ""
<<<<<<< HEAD
        )
        return last_messages

    async def message_reactions(self, message_id: int) -> Sequence[Reaction]:
=======
        ]
        return last_messages

    async def message_reactions(self, message_id: int) -> list[Reaction]:
>>>>>>> 40ddd30a2222e07214cb285f275da7dff0b36a58
        """Возвращает список реакций для конкретного сообщения."""
        url = f"{API_ROOT}/messages/{message_id}/reactions"
        return await self._get_objects(url, Reaction)
