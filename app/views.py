import json
from abc import ABC
from datetime import datetime

from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import SensorData
from app.serializers import SensorDataSerializer, FakeSensorDataSerializer, LineChartDataSerializer
from app.random_mockup import RandomFakeData
from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import PageNumberPagination

from .utils import download_csv
from django.http import HttpResponse


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
        if "page" in query_condition:
            del query_condition["page"]
        return queryset.filter(**query_condition)


class DataTable(ListAPIView):
    queryset = SensorData.objects.all()
    filter_backends = [SearchFilterBackend,]
    serializer_class = SensorDataSerializer
    pagination_class = PageNumberPagination


class LineChartView(ListAPIView):
    # serializer_class = LineChartDataSerializer
    # queryset = SensorData.objects.all()
    # filter_backends = [SearchFilterBackend, ]
    def get(self, request, *args, **kwargs):
        queryset = SensorData.objects.all().order_by("sensor_datetime")
        ser = LineChartDataSerializer(instance=queryset, many=True)
        linechart_dict = dict()
        linechart_dict["station_num"] = list()
        linechart_dict["sensor_datetime"] = list()
        linechart_dict["temperature"] = list()
        linechart_dict["wind_speed"] = list()
        linechart_dict["pressure"] = list()
        linechart_dict["solar_radiation"] = list()
        for item in ser.data:
            linechart_dict["station_num"].append(item.get("station_num"))
            linechart_dict["sensor_datetime"].append(datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                                                          "%Y-%m-%dT%H:%M:%SZ"))*1000)

            linechart_dict["temperature"].append(item.get("temperature"))
            linechart_dict["wind_speed"].append(item.get("wind_speed"))
            linechart_dict["pressure"].append(item.get("pressure"))
            linechart_dict["solar_radiation"].append(item.get("solar_radiation"))

        return Response(linechart_dict)


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


# def download(request):
#     data = download_csv(request, SensorData.objects.all())
#     return HttpResponse(data, content_type='text/csv')

class Download(APIView):

    def get(self, request, *args, **kwargs):
        query_condition = dict()
        for k, v in request.query_params.dict().items():
            query_condition[k] = v
        queryset = SensorData.objects.all().filter(**query_condition)
        data = download_csv(request, queryset)
        return HttpResponse(data, content_type='text/csv')
