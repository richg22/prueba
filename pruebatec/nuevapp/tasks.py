from celery import shared_task
from cruds.utils import handlesendemail


@shared_task
def send_async_email(email, id):
    handlesendemail(email, id)
    return
