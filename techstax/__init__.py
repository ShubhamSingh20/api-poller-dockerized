from environs import Env

env = Env()
env.read_env() 

MONGO_DB = env.str('MONGO_DB')
MONGO_URL = env.str('MONGO_URL')
RABBIT_MQ_URL = env.str('RABBIT_MQ_URL')
POLLER_SCHEDULER_SECONDS = env.float('POLLER_SCHEDULER_SECONDS')

import logging

logging.basicConfig(filename="error.log", level=logging.ERROR)
logger = logging.getLogger(__name__)
