from json import JSONDecodeError
from datetime import datetime, timedelta

from httpx import AsyncClient, Response

from pachka_watcher.exceptions import JSONError
from pachka_watcher.integrations.client import AsyncPachkaClient
from pachka_watcher.schemas.messages import Message, Reaction

API_ROOT = 'https://api.pachca.com/api/shared/v1'
MESSAGES_PER_PAGE = 50


class PachkaService:
    """Сервис для работы с Pachka."""

    def __init__(self, client: AsyncClient):
        self.client = client

    def _check_response(self, response: Response) -> Response:
        """Проверяет ответ на корректность."""
        try:
            response = response.json()
        except (JSONDecodeError, TypeError) as e:
            raise JSONError(f'Ошибка при обработке ответа: {e}')

        if 'data' not in response:
            raise KeyError('Пустой ответ. Нет ключа data')
        return response

    async def get_chat_messages(self, chat_id: int) -> list[Message]:
        """Возвращает список сообщений для конкретного чата."""
        url = f'{API_ROOT}/messages?chat_id={chat_id}&per={MESSAGES_PER_PAGE}'

        response = self._check_response(
            await self.client.get(url)
        )

        return [Message(**message) for message in response['data']]
    
    async def get_recent_messages(self, chat_id: int, hours: int = 60) -> list[Message]:
        """Возвращает список последних сообщений за hours для конкретного чата."""
        messages = await self.get_chat_messages(chat_id)
        last_messages = [
            message
            for message in messages
            if message.created_at.timestamp()
            >= (datetime.now() - timedelta(hours=hours)).timestamp() and 
            message.content != ''
        ]
        
        return last_messages
    
    async def message_reactions(self, message_id: int) -> list[Reaction]:
        """Возвращает список реакций для конкретного сообщения."""
        url = f'{API_ROOT}//messages/{message_id}/reactions'

        response = self._check_response(
            await self.client.get(url)
        )

        return [Reaction(**reaction) for reaction in response['data']]