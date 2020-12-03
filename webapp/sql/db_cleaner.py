from datetime import datetime, timedelta
from stockapp.models import Diary
from webapp.sql.db_sql import Sql


def db_clean_stocks():
    diaries = Diary.objects.filter(diary_remove__isnull=False)
    for diary in diaries:
        if datetime.now().date() >= diary.diary_remove + timedelta(days=90):
            Sql.destroy_stock(diary)
