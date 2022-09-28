import json
import time
from abc import ABC
from datetime import datetime

from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import SensorData
from app.serializers import SensorDataSerializer, FakeSensorDataSerializer, LineChartDataSerializer, \
    BarChartDataSerializer, TemperatureLineChartDataSerializer, WindSpeedLineChartDataSerializer, \
    PressureLineChartDataSerializer, SolarRadiationLineChartDataSerializer
from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import PageNumberPagination

from .utils import download_csv
from django.http import HttpResponse


def group_by_station(ser,data_name):
    linechart_dict = dict()
    for i in range(1, 6):
        linechart_dict["station" + str(i)] = list()

    for item in ser.data:
        if item.get("station") == "231824A":
            linechart_dict["station1"].append([
                datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                     "%Y-%m-%dT%H:%M:%SZ")) * 1000,
                item.get(data_name),
                item.get("station")])
        elif item.get("station") == "231825A":
            linechart_dict["station2"].append([
                datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                     "%Y-%m-%dT%H:%M:%SZ")) * 1000,
                item.get(data_name),
                item.get("station")])
        elif item.get("station") == "231826A":
            linechart_dict["station3"].append([
                datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                     "%Y-%m-%dT%H:%M:%SZ")) * 1000,
                item.get(data_name),
                item.get("station")])
        elif item.get("station") == "231827A":
            linechart_dict["station4"].append([
                datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                     "%Y-%m-%dT%H:%M:%SZ")) * 1000,
                item.get(data_name),
                item.get("station")])
        elif item.get("station") == "231828A":
            linechart_dict["station5"].append([
                datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                     "%Y-%m-%dT%H:%M:%SZ")) * 1000,
                item.get(data_name),
                item.get("station")])
    return linechart_dict

class SearchFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        query_condition = dict()
        for k, v in request.query_params.dict().items():
            query_condition[k] = v
        if "page" in query_condition:
            del query_condition["page"]
        if "start_time" in query_condition and "end_time" in query_condition:
            start_time_str = query_condition["start_time"]
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            print(start_time)
            del query_condition["start_time"]
            end_time_str = query_condition["end_time"]
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            print(end_time)
            del query_condition["end_time"]
            queryset = queryset.filter(sensor_datetime__range=[start_time, end_time])
        queryset = queryset.filter(**query_condition)

        return queryset


class DataTable(ListAPIView):
    """
        view class for data display function and data query function.
        GET:
        If there is query condition, this view will return the query result to the frontend.
        If there is not a query condition, this view will return all the data to the frontend.
        :return Response(serializer.data)
    """
    queryset = SensorData.objects.all()
    filter_backends = [SearchFilterBackend, ]
    serializer_class = SensorDataSerializer
    pagination_class = PageNumberPagination


class LineChartView(ListAPIView):
    """
        view class for line chart function.
        GET:
        return the station, sensor_datetime, temperature, wind_speed,
        pressure and solar_radiation columns from the database.
        :return Response(linechart_dict{"station":[], "sensor_datetime":[], "temperature":[], "wind_speed":[],
        "pressure":[], "solar_radiation":[]})
    """
    def get(self, request, *args, **kwargs):
        queryset = SensorData.objects.all().order_by("sensor_datetime")[0:1000]
        ser = LineChartDataSerializer(instance=queryset, many=True)
        linechart_dict = dict()
        linechart_dict["station"] = list()
        linechart_dict["sensor_datetime"] = list()
        linechart_dict["temperature"] = list()
        linechart_dict["wind_speed"] = list()
        linechart_dict["pressure"] = list()
        linechart_dict["solar_radiation"] = list()
        for item in ser.data:
            linechart_dict["station"].append(item.get("station"))
            linechart_dict["sensor_datetime"].append(datetime.timestamp(datetime.strptime(item.get("sensor_datetime"),
                                                                                          "%Y-%m-%dT%H:%M:%SZ")) * 1000)
            linechart_dict["temperature"].append(item.get("temperature"))
            linechart_dict["wind_speed"].append(item.get("wind_speed"))
            linechart_dict["pressure"].append(item.get("pressure"))
            linechart_dict["solar_radiation"].append(item.get("solar_radiation"))

        return Response(linechart_dict)


class LineChartSearchFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        query_condition = dict()
        for k, v in request.query_params.dict().items():
            query_condition[k] = v
        if "start_time" in query_condition and "end_time" in query_condition:
            start_time_str = query_condition["start_time"]
            start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M')
            print(start_time)
            del query_condition["start_time"]
            end_time_str = query_condition["end_time"]
            end_time = datetime.strptime(end_time_str, '%Y-%m-%dT%H:%M')
            print(end_time)
            del query_condition["end_time"]
            queryset = queryset.filter(sensor_datetime__range=[start_time, end_time])
            return queryset
        return queryset[0:10000]




class TemperatureLineChartView(ListAPIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, *args, **kwargs):
            ser = TemperatureLineChartDataSerializer(instance=self.get_queryset(), many=True)
            linechart_dict = group_by_station(ser, "temperature")
            return Response(linechart_dict)


class WindSpeedLineChartView(ListAPIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, *args, **kwargs):
            ser = WindSpeedLineChartDataSerializer(instance=self.get_queryset(), many=True)
            linechart_dict = group_by_station(ser, "wind_speed")
            return Response(linechart_dict)


class PressureLineChartView(ListAPIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, *args, **kwargs):
            ser = PressureLineChartDataSerializer(instance=self.get_queryset(), many=True)
            linechart_dict = group_by_station(ser, "pressure")
            return Response(linechart_dict)


class SolarRadiationLineChartView(ListAPIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, *args, **kwargs):
            ser = SolarRadiationLineChartDataSerializer(instance=self.get_queryset(), many=True)
            linechart_dict = group_by_station(ser, "solar_radiation")
            return Response(linechart_dict)

class BarChartView(APIView):

    def get(self, request, *arg, **kwargs):
        queryset = SensorData.objects.all()[0:10000]
        ser = BarChartDataSerializer(instance=queryset, many=True)
        barchart_dict = {
            "rainfall": [item.get("rainfall") for item in ser.data],
            "humidity": [item.get("humidity") for item in ser.data],
        }
        return Response(barchart_dict)


class FakeData(APIView):

    def post(self, request, *args, **kwargs):
        with open("summer-2021-2022-2m-stations.txt", "r") as data_file:
            data = data_file.readlines()
        data_list_insert = list()
        for line in data[1:]:
            line = line.strip('\n')
            line_list = line.split(',')
            line_null_list = [ None if i == "" else i for i in line_list ]

            temp_dict = SensorData()
            temp_dict.sensor_datetime = line_null_list[0]
            temp_dict.rainfall = line_null_list[1]
            temp_dict.rainfall_quality = line_null_list[2]
            temp_dict.temperature = line_null_list[3]
            temp_dict.temperature_quality = line_null_list[4]
            temp_dict.humidity = line_null_list[5]
            temp_dict.humidity_quality = line_null_list[6]
            temp_dict.wind_direction = line_null_list[7]
            temp_dict.wind_direction_quality = line_null_list[8]
            temp_dict.wind_speed = line_null_list[9]
            temp_dict.wind_speed_quality = line_null_list[10]
            temp_dict.pressure = line_null_list[11]
            temp_dict.pressure_quality = line_null_list[12]
            temp_dict.solar_radiation = line_null_list[13]
            temp_dict.solar_radiation_quality = line_null_list[14]
            temp_dict.station = line_null_list[15]
            data_list_insert.append(temp_dict)

        for i in range(0, len(data_list_insert), 10000):
            SensorData.objects.bulk_create(data_list_insert[i: i + 10000])
        return Response("successful")


class Download(APIView):
    filter_backends = [SearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    """
        view class for data download function.
        GET:
        If there is query condition in request, this view will download the query result as a csv file.
        If there is not a query condition, this view will download all the data as a csv file.
        :return HttpResponse(data, content_type='text/csv')
    """
    def get(self, request, *args, **kwargs):
        data = download_csv(request, self.get_queryset())
        response = HttpResponse(data, content_type='text/csv')
        file_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".csv"
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
        return response