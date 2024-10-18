import asyncio

from pachka_watcher.integrations.client import AsyncPachkaClient
from pachka_watcher.services.pachka import PachkaService
from pachka_watcher.settings import settings


async def run():
    client = AsyncPachkaClient(settings)
    service = PachkaService(client)
    result = await service.message_reactions(358223713)
    print(*result, sep='\n-----------\n')


def main():
    asyncio.run(run())


if __name__ == '__main__':
    main()