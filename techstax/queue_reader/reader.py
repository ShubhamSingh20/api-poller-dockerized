import asyncio
import motor.motor_asyncio
from techstax import MONGO_DB, MONGO_URL, logger

class DBWriter(object):
    """
        DBWriter implements methods for storing data into, mongo server
        it takes the connection url & dbname as argument
    """
    def __init__(self, mongo_url, db) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            mongo_url, connectTimeoutMS=30000, 
            socketTimeoutMS=None, socketKeepAlive=True, 
            connect=False, maxPoolsize=1
        )
        self.db = self.client[db]

    async def write_to_db(self, document : dict) -> None:
        try:
            await self.db.collection.insert_one(document)
        except Exception as ex:
            logger.error(ex.args)

class QueueReader(object):
    """
        An implementation of a consumer that takes data from the broker
        and writes that data into a mongo server
    """

    def __init__(self, data : dict) -> None:
        self.data = data
        self.writer = DBWriter(mongo_url=MONGO_URL, db=MONGO_DB)

    def run(self) -> None:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.writer.write_to_db(self.data))
