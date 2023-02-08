from celery import shared_task
from .parsing import theand

@shared_task
def bar():
    return theand()