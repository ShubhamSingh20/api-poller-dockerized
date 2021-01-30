from ..celery import celery
from .reader import QueueReader

@celery.task
def queue_reader_task(data : dict):
    QueueReader(data=data).run()
