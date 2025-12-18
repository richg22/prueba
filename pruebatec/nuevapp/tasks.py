from celery import shared_task
from cruds.utils import handlesendemail

@shared_task
def test():
    handlesendemail()
    return