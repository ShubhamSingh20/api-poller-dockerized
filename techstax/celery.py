import os 
from celery import Celery
from techstax import POLLER_SCHEDULER_SECONDS, RABBIT_MQ_URL

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

celery = Celery('techstax', broker=RABBIT_MQ_URL)

celery.autodiscover_tasks([
    'techstax.api_poller', 
    'techstax.queue_reader'
])

celery.conf.beat_schedule = {
    'run-every-n-second': {
        'task': 'techstax.api_poller.poll_api_task',
        'schedule': POLLER_SCHEDULER_SECONDS,
    },
}