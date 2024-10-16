import asyncio

from pachka_watcher.integrations.client import AsyncPachkaClient
from pachka_watcher.settings import settings


async def run():
    client = AsyncPachkaClient(settings)
    result = await client.get(
        'https://api.pachca.com/api/shared/v1/chats'
    )
    print(result.json())


def main():
    asyncio.run(run())


if __name__ == '__main__':
    main()