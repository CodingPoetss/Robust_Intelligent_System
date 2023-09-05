from django.db import models
from datetime import datetime
from accounts.models import UserInfo


# Create your models here.
class LicensePlateInfo(models.Model):
    user = models.CharField(verbose_name='用户', max_length=32, default='用户已注销')
    plate_number = models.CharField(verbose_name='车牌号', max_length=10)
    recognition_time = models.DateTimeField(verbose_name='识别时间', default=datetime.now())
    file = models.FileField(upload_to='images/', verbose_name='文件')
