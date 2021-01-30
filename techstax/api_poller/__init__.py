from .poller import Poller
from ..celery import celery

@celery.task
def poll_api_task():
    Poller([
        'https://randomuser.me/api/',
        'https://www.thecocktaildb.com/api/json/v1/1/random.php',
    ]).run()
