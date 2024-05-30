from django.db import models

class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)

    def __str__(self):
        return self.username

class AdminInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=128)

    def __str__(self):
        return self.username
