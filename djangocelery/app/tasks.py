from celery import shared_task
import time

@shared_task
def celery_task(counter):
    email = "cser.sandeepsingh@gmail.com"
    time.sleep(30)
    return ('{0} Done!'.format(counter))