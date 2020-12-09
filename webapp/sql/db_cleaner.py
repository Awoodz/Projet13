from datetime import datetime, timedelta

from stockapp.models import Diary
from webapp.sql.db_sql import Sql


def db_clean_stocks():
    """Remove oldest diary/notification/stock from database"""
    # Filters diaries where product was removed from stock
    diaries = Diary.objects.filter(diary_remove__isnull=False)
    for diary in diaries:
        # If diary is older than 3 months, delete the stock from database
        if datetime.now().date() >= diary.diary_remove + timedelta(days=90):
            Sql.destroy_stock(diary)
