# Generated by Django 4.2.11 on 2024-05-29 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0005_alter_licenseplateinfo_recognition_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licenseplateinfo',
            name='recognition_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 30, 3, 22, 23, 466604), verbose_name='识别时间'),
        ),
    ]