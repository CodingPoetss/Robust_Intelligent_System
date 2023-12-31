# Generated by Django 4.2.4 on 2023-08-31 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LicensePlateInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "owner",
                    models.CharField(
                        default="unknown", max_length=10, verbose_name="车主"
                    ),
                ),
                ("plate_number", models.CharField(max_length=10, verbose_name="车牌号")),
                ("recognition_time", models.DateTimeField(verbose_name="识别时间")),
            ],
        ),
    ]
