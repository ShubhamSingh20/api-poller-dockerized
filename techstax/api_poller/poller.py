import asyncio
import aiohttp
import logging
from typing import Any
from ..celery import celery
from techstax import logger

class Poller(object):
    """
        Poller will be called using a beat task worker, which would ensure
        consistency accross multiple workers and queues.
    """
    def __init__(self, urls : list) -> None:
        self.urls = urls
        self.queue_reader_task = 'techstax.queue_reader.queue_reader_task'

    async def make_api_call(self, url) -> Any:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    return await response.json()
        except Exception as ex:
            logger.error(ex.args)
        return None

    def initiate_queue_reader(self, data) -> None:
        celery.send_task(name=self.queue_reader_task, args=[data])

    def run(self) -> None:
        loop = asyncio.get_event_loop()
        url_routines = [self.make_api_call(url) for url in self.urls]
        results = loop.run_until_complete(asyncio.gather(*url_routines))

        for res in results:
            if res is not None:
                self.initiate_queue_reader(data=res)
