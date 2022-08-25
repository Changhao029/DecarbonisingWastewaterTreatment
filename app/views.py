import json
from abc import ABC

from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import SensorData
from app.serializers import SensorDataSerializer, FakeSensorDataSerializer
from app.random_mockup import RandomFakeData
from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import PageNumberPagination


# class DataTable(APIView):
#
#     def get(self, request, *args, **kwargs):
#         if request.query_params:
#             queryset = SensorData.objects.filter(**request.query_params).first()
#             ser = SensorDataSerializer(instance=queryset, many=False)
#         else:
#             queryset = SensorData.objects.all()
#             ser = SensorDataSerializer(instance=queryset, many=True)
#         return Response({"result": ser.data})


class SearchFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        query_condition = dict()
        for k, v in request.query_params.dict().items():
            query_condition[k] = v
        del query_condition["page"]
        return queryset.filter(**query_condition)


class DataTable(ListAPIView):
    queryset = SensorData.objects.all()
    filter_backends = [SearchFilterBackend,]
    serializer_class = SensorDataSerializer
    pagination_class = PageNumberPagination


class FakeData(APIView):

    def post(self, request, *args, **kwargs):
        RM = RandomFakeData()
        for i in range(1000):
            temp_dict = SensorData()
            temp_dict.sensor_datetime = RM.random_date()
            temp_dict.rainfall = RM.random_float(decimal=2)
            temp_dict.rainfall_quality = RM.random_int()
            temp_dict.temperature = RM.random_float(decimal=1)
            temp_dict.temperature_quality = RM.random_int()
            temp_dict.humidity = RM.random_float(decimal=1)
            temp_dict.humidity_quality = RM.random_int()
            temp_dict.wind_direction = RM.random_int()
            temp_dict.wind_direction_quality = RM.random_int()
            temp_dict.wind_speed = RM.random_float(decimal=2)
            temp_dict.wind_speed_quality = RM.random_int()
            temp_dict.pressure = RM.random_float(decimal=1)
            temp_dict.pressure_quality = RM.random_int()
            temp_dict.solar_radiation = RM.random_float(decimal=1)
            temp_dict.solar_radiation_quality = RM.random_int()
            temp_dict.station = RM.random_station()
            temp_dict.save()
        return Response("successful")