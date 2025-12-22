from celery import shared_task
from cruds.utils import handlesendemail, handlesendwinneremail


@shared_task
def send_async_email(email, id):
    handlesendemail(email, id)
    return


@shared_task
def send_winner_email(email):
    handlesendwinneremail(email)
    return
