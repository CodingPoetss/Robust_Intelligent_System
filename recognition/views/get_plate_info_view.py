# author: CodingPoetss
# coding time: 2024/2/21 22:42
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import LicensePlateInfo
from ..serializers import GetPlateInfoSerializer
from rest_framework.pagination import PageNumberPagination


class GetPlateInfoView(APIView, PageNumberPagination):
    page_size = 10

    def get(self, request, *args, **kwargs):
        persons = LicensePlateInfo.objects.all().order_by("id")
        result_page = self.paginate_queryset(persons, request, view=self)
        serializer = GetPlateInfoSerializer(result_page, many=True)
        return self.get_paginated_response(serializer.data)
