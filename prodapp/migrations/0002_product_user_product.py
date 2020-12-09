# Generated by Django 3.1.3 on 2020-12-03 10:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prodapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
