# author: CodingPoetss
# coding time: 2024/2/21 22:43
from rest_framework import serializers
from .models import LicensePlateInfo


class GetPlateInfoSerializer(serializers.ModelSerializer):
    recognition_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = LicensePlateInfo
        fields = ('id', 'user', 'plate_number', 'recognition_time', 'file')
