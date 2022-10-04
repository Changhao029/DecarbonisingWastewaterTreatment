import json
import time
from abc import ABC
from datetime import datetime

from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from rest_framework.request import Request
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import SensorData
from app.serializers import SensorDataSerializer, FakeSensorDataSerializer, LineChartDataSerializer, \
    BarChartDataSerializer, TemperatureLineChartDataSerializer, WindSpeedLineChartDataSerializer, \
    PressureLineChartDataSerializer, SolarRadiationLineChartDataSerializer, WindRoseChartDataSerializer
from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import PageNumberPagination

from .utils import download_csv
from django.http import HttpResponse


def group_by_station(ser, data_name):
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


# def group_by_station_wind_rose(ser, data_name):
#     result = dict()
#     max_value = 0
#     windroos_list = list()
#     windrose_dict = dict()
#     for i in range(0, 5):
#         # 'N', 'WN', 'W', 'SW', 'S', 'ES', 'E', 'NE'
#         windrose_dict["23182" + str(i + 4) + "A"] = list([0, 0, 0, 0, 0, 0, 0, 0])
#
#     for item in ser.data:
#         station_str = item.get("station")
#         if item.get(data_name):
#             if item.get(data_name) <= 22.5 or item.get(data_name) > 337.5:
#                 windrose_dict[station_str][0] = windrose_dict[station_str][0] + 1
#             elif 22.5 < item.get(data_name) <= 67.5:
#                 windrose_dict[station_str][1] = windrose_dict[station_str][1] + 1
#             elif 67.5 < item.get(data_name) <= 112.5:
#                 windrose_dict[station_str][2] = windrose_dict[station_str][2] + 1
#             elif 112.5 < item.get(data_name) <= 157.5:
#                 windrose_dict[station_str][3] = windrose_dict[station_str][3] + 1
#             elif 157.5 < item.get(data_name) <= 202.5:
#                 windrose_dict[station_str][4] = windrose_dict[station_str][4] + 1
#             elif 202.5 < item.get(data_name) <= 247.5:
#                 windrose_dict[station_str][5] = windrose_dict[station_str][5] + 1
#             elif 247.5 < item.get(data_name) <= 292.5:
#                 windrose_dict[station_str][6] = windrose_dict[station_str][6] + 1
#             else:
#                 windrose_dict[station_str][7] = windrose_dict[station_str][7] + 1
#
#     for k, v in windrose_dict.items():
#         windroos_list.append({"name": k, "value": v})
#         if max_value < max(v):
#             max_value = max(v)
#     while max_value % 50 != 0:
#         max_value = max_value + 1
#     result["data_result"] = windroos_list
#     result["max_value"] = max_value
#     return result

def group_by_station_wind_rose(ser, wind_speed, wind_direction, count):
    print(count)
    wind_speed_dict = dict()
    for i in range(0, 7):
        # 'N', 'WN', 'W', 'SW', 'S', 'ES', 'E', 'NE'
        wind_speed_dict[i] = list([0, 0, 0, 0, 0, 0, 0, 0])

    for item in ser.data:
        if item.get(wind_speed) and item.get(wind_direction):
            if float(item.get(wind_speed)) <= 1:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[0][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[0][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[0][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[0][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[0][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[0][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[0][6] += 1
                else:
                    wind_speed_dict[0][7] += 1
            elif 1 <= float(item.get(wind_speed)) < 2:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[1][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[1][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[1][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[1][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[1][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[1][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[1][6] += 1
                else:
                    wind_speed_dict[1][7] += 1
            elif 2 <= float(item.get(wind_speed)) < 4:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[2][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[2][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[2][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[2][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[2][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[2][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[2][6] += 1
                else:
                    wind_speed_dict[2][7] += 1
            elif 4 <= float(item.get(wind_speed)) < 6:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[3][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[3][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[3][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[3][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[3][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[3][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[3][6] += 1
                else:
                    wind_speed_dict[3][7] += 1
            elif 6 <= float(item.get(wind_speed)) < 8:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[4][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[4][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[4][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[4][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[4][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[4][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[4][6] += 1
                else:
                    wind_speed_dict[4][7] += 1
            elif 8 <= float(item.get(wind_speed)) < 10:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[5][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[5][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[5][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[5][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[5][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[5][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[5][6] += 1
                else:
                    wind_speed_dict[5][7] += 1
            else:
                if item.get(wind_direction) <= 22.5 or item.get(wind_direction) > 337.5:
                    wind_speed_dict[6][0] += 1
                elif 22.5 < item.get(wind_direction) <= 67.5:
                    wind_speed_dict[6][1] += 1
                elif 67.5 < item.get(wind_direction) <= 112.5:
                    wind_speed_dict[6][2] += 1
                elif 112.5 < item.get(wind_direction) <= 157.5:
                    wind_speed_dict[6][3] += 1
                elif 157.5 < item.get(wind_direction) <= 202.5:
                    wind_speed_dict[6][4] += 1
                elif 202.5 < item.get(wind_direction) <= 247.5:
                    wind_speed_dict[6][5] += 1
                elif 247.5 < item.get(wind_direction) <= 292.5:
                    wind_speed_dict[6][6] += 1
                else:
                    wind_speed_dict[6][7] += 1

    for i in range(0,7):
        for j in range(0,8):
            wind_speed_dict[i][j] = round((wind_speed_dict[i][j] / count) * 100, 2)

    return wind_speed_dict


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


@method_decorator(gzip_page, name='dispatch')
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


@method_decorator(gzip_page, name='dispatch')
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


@method_decorator(gzip_page, name='dispatch')
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


@method_decorator(gzip_page, name='dispatch')
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


class rainfall_BarChartView(APIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, *arg, **kwargs):
        start_time = self.get_queryset()[0].sensor_datetime.strftime("%Y-%m-%d %H:%M:%S")
        end_time = self.get_queryset()[len(self.get_queryset()) - 1].sensor_datetime.strftime("%Y-%m-%d %H:%M:%S")

        ser = BarChartDataSerializer(instance=self.get_queryset(), many=True)
        rainfall_total = dict()
        for item in ser.data:
            date_t = datetime.strptime(item.get("sensor_datetime"), "%Y-%m-%dT%H:%M:%SZ")
            key_id = date_t.year * 372 + date_t.month * 31 + date_t.day
            r_value_id = item.get("rainfall")
            if r_value_id is None:
                r_value_id = 0
            if key_id not in rainfall_total:
                rainfall_total[key_id] = float(r_value_id)
            rainfall_total[key_id] += float(r_value_id)
        sorted(rainfall_total)
        return Response({"data": rainfall_total, "start_t": start_time, "end_t": end_time})


class humidity_BarChartView(APIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get(self, request, *arg, **kwargs):
        start_time = self.get_queryset()[0].sensor_datetime.strftime("%Y-%m-%d %H:%M:%S")
        end_time = self.get_queryset()[len(self.get_queryset()) - 1].sensor_datetime.strftime("%Y-%m-%d %H:%M:%S")

        ser = BarChartDataSerializer(instance=self.get_queryset(), many=True)
        humidity_total = dict()
        humidity_total_result = dict()
        for item in ser.data:
            date_t = datetime.strptime(item.get("sensor_datetime"), "%Y-%m-%dT%H:%M:%SZ")
            key_id = date_t.year * 372 + date_t.month * 31 + date_t.day
            h_value_id = item.get("humidity")
            if h_value_id is None:
                h_value_id = 0
            if key_id not in humidity_total:
                humidity_total[key_id] = [float(h_value_id), 1]
            humidity_total[key_id][0] += float(h_value_id)
            humidity_total[key_id][1] += 1
        for k,v in humidity_total.items():
            humidity_total_result[k] = v[0]/v[1]
        sorted(humidity_total_result)
        # return Response(humidity_total_result)
        return Response({"data": humidity_total_result, "start_t": start_time, "end_t": end_time})


class WindRoseChartView(APIView):
    filter_backends = [LineChartSearchFilterBackend, ]

    def get_queryset(self):
        """Return the last five published polls."""
        queryset = SensorData.objects.all()
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset


    def get(self, request, *args, **kwargs):
        start_time = self.get_queryset()[0].sensor_datetime.strftime("%Y-%m-%d %H:%M:%S")
        end_time = self.get_queryset()[len(self.get_queryset())-1].sensor_datetime.strftime("%Y-%m-%d %H:%M:%S")

        ser = WindRoseChartDataSerializer(instance=self.get_queryset(), many=True)
        linechart_dict = group_by_station_wind_rose(ser, "wind_speed", "wind_direction", len(self.get_queryset()))
        return Response({"data": linechart_dict, "start_time": start_time, "end_time": end_time})


class FakeData(APIView):

    def post(self, request, *args, **kwargs):
        with open("summer-2021-2022-2m-stations.txt", "r") as data_file:
            data = data_file.readlines()
        data_list_insert = list()
        for line in data[1:]:
            line = line.strip('\n')
            line_list = line.split(',')
            line_null_list = [None if i == "" else i for i in line_list]

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
