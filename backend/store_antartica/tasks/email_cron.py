from celery import shared_task
from management.commands import scraper_antartica,scraper_buscalibre
@shared_task
def email_cron():
    
    pass