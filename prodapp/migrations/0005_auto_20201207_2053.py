# Generated by Django 3.1.3 on 2020-12-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodapp', '0004_merge_20201203_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_name',
            field=models.CharField(max_length=100),
        ),
    ]
