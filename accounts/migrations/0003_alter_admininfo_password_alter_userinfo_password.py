# Generated by Django 4.2.11 on 2024-05-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_admininfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admininfo',
            name='password',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=128, verbose_name='密码'),
        ),
    ]