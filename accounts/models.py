from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username       # 实例化对象时输出的是地址,__str__(self)可以打印具体的名称


class AdminInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username       # 实例化对象时输出的是地址,__str__(self)可以打印具体的名称
