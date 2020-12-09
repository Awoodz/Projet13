from django.db import models

from userapp.models import CustomUser


class AppNews(models.Model):
    news_title = models.CharField(max_length=50, unique=False,)
    news_date = models.DateField(auto_now=False, auto_now_add=False)
    news_content = models.TextField()
    news_author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
