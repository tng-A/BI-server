from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from src.api.helpers.transactions import transactions_update


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(transactions_update, 'interval', hours=2)
    scheduler.start()
