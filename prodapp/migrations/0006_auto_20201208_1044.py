# Generated by Django 3.1.3 on 2020-12-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodapp', '0005_auto_20201207_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
