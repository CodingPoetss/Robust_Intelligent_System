# python learning
# coding time: 2023/8/23 15:37
from django.conf import settings
import hashlib


def md5(data_string):
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))  # 盐，用于混淆的乱码
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()