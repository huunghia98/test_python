from celery import Celery
import requests

CELERY_RESULT_BACKEND = 'amqp://huunghia98:nghia123@localhost/flask_login_host'
CELERY_BROKER_URL = 'amqp://huunghia98:nghia123@localhost/flask_login_host'


def make_celery():
    celery = Celery(
        name='celery_task',
        backend=CELERY_RESULT_BACKEND,
        broker=CELERY_BROKER_URL
    )
    return celery


worker = make_celery()


@worker.task
def download(site):
    session = requests.session()
    with session.get(site) as response:
        print(f"Read {len(response.content)} from {site}")
