from json import JSONDecodeError

from httpx import AsyncClient

from pachka_watcher.exceptions import JSONError
from pachka_watcher.integrations.client import AsyncPachkaClient
from pachka_watcher.schemas.messages import Message

API_ROOT = 'https://api.pachca.com/api/shared/v1/'
MESSAGES_PER_PAGE = 50


class PachkaService:
    """Сервис для работы с Pachka."""

    def __init__(self, client: AsyncClient):
        self.client = client

    async def get_chat_messages(self, chat_id: int) -> list[Message]:
        """Возвращает список сообщений для конкретного чата."""
        url = f'{API_ROOT}/messages?chat_id={chat_id}&per={MESSAGES_PER_PAGE}'

        response = (await self.client.get(url))

        try:
            response = response.json()
        except (JSONDecodeError, TypeError) as e:
            raise JSONError(f'Ошибка при обработке ответа: {e}')

        if 'data' not in response:
            raise KeyError('Пустой ответ. Нет ключа data')

        return [Message(**message) for message in response['data']]
    
    