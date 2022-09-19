import os, django

from django.test import TestCase
from django.test.client import Client
from app.models import SensorData

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()


# class ModelTest(TestCase):
#     def setUp(self):
#         SensorData.objects.create(sensor_datetime='2021-11-30 00:00:30',
#                                   rainfall=None,
#                                   rainfall_quality=None,
#                                   temperature=None,
#                                   temperature_quality=None,
#                                   humidity=None,
#                                   humidity_quality=None,
#                                   wind_direction=None,
#                                   wind_direction_quality=None,
#                                   wind_speed=None,
#                                   wind_speed_quality=None,
#                                   pressure=None,
#                                   pressure_quality=None,
#                                   solar_radiation=None,
#                                   solar_radiation_quality=None,
#                                   station="231825A",
#                                   )
#
#     def test_query(self):
#         result = SensorData.objects.filter(station="231825A").first()
#         self.assertEqual(result.station, "231825A")


class DataTableTest(TestCase):
    def setUp(self):
<<<<<<< HEAD
        self.base_url = '/datatable/?page=1'
=======
        self.data_query_all_url = '/datatable/?page=1'
        self.data_query_one_url = '/datatable/?station=231825A'
        self.data_query_none_url = '/datatable/?station=23'
>>>>>>> f5ed34c7edf7bad9c8b800dfd3907b13663ddc02
        SensorData.objects.create(sensor_datetime='2021-11-30 00:00:30',
                                  rainfall=None,
                                  rainfall_quality=None,
                                  temperature=None,
                                  temperature_quality=None,
                                  humidity=None,
                                  humidity_quality=None,
                                  wind_direction=None,
                                  wind_direction_quality=None,
                                  wind_speed=None,
                                  wind_speed_quality=None,
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231825A",
                                  )
<<<<<<< HEAD
        SensorData.objects.create(sensor_datetime='2021-11-30 23:45:00',
                                  rainfall=1,
                                  rainfall_quality=None,
                                  temperature=None,
                                  temperature_quality=None,
                                  humidity=76.7,
                                  humidity_quality=147,
                                  wind_direction=329,
                                  wind_direction_quality=1,
                                  wind_speed=4.73,
                                  wind_speed_quality=50,
                                  pressure=1010.2,
                                  pressure_quality=1,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231827A",
                                  )
        SensorData.objects.create(sensor_datetime='2021-11-30 23:46:00',
                                  rainfall=1,
                                  rainfall_quality=None,
                                  temperature=21.0,
                                  temperature_quality=1,
                                  humidity=70.3,
                                  humidity_quality=147,
                                  wind_direction=344,
                                  wind_direction_quality=1,
                                  wind_speed=2.5,
                                  wind_speed_quality=50,
=======

    def test_data_query_all(self):
        c = Client()
        response = c.get(self.data_query_all_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], len(SensorData.objects.all()))

    def test_data_query_one(self):
        c = Client()
        response = c.get(self.data_query_one_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["station"], "231825A")

    def test_data_query_none(self):
        c = Client()
        response = c.get(self.data_query_none_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)


class LineChartTest(TestCase):
    def setUp(self):
        self.line_chart_url = '/linechart/'
        SensorData.objects.create(sensor_datetime='2021-11-30 00:00:30',
                                  rainfall=None,
                                  rainfall_quality=None,
                                  temperature=None,
                                  temperature_quality=None,
                                  humidity=None,
                                  humidity_quality=None,
                                  wind_direction=None,
                                  wind_direction_quality=None,
                                  wind_speed=None,
                                  wind_speed_quality=None,
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231825A",
                                  )
        SensorData.objects.create(sensor_datetime='2021-11-30 00:00:30',
                                  rainfall=None,
                                  rainfall_quality=None,
                                  temperature=None,
                                  temperature_quality=None,
                                  humidity=None,
                                  humidity_quality=None,
                                  wind_direction=None,
                                  wind_direction_quality=None,
                                  wind_speed=None,
                                  wind_speed_quality=None,
>>>>>>> f5ed34c7edf7bad9c8b800dfd3907b13663ddc02
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231826A",
                                  )
<<<<<<< HEAD

    def test_query_all(self):
        c = Client()
        response = c.get(self.base_url)

        self.assertEqual(response.status_code, 200)

    def test_barchart(self):
        c = Client()
        response = c.get('/barchart/')
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, dict))
        self.assertTrue('rainfall' in response.data)
        self.assertTrue('humidity' in response.data)
        self.assertTrue(isinstance(response.data['rainfall'], list))
        self.assertTrue(isinstance(response.data['humidity'], list))
=======
        SensorData.objects.create(sensor_datetime='2021-11-30 00:00:30',
                                  rainfall=None,
                                  rainfall_quality=None,
                                  temperature=None,
                                  temperature_quality=None,
                                  humidity=None,
                                  humidity_quality=None,
                                  wind_direction=None,
                                  wind_direction_quality=None,
                                  wind_speed=None,
                                  wind_speed_quality=None,
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231827A",
                                  )

    def test_data_query_all(self):
        c = Client()
        response = c.get(self.line_chart_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["station"]), 3)


from django.http.response import HttpResponse
class DownloadTest(TestCase):
    def setUp(self):
        self.download_url = '/download/'
        SensorData.objects.create(sensor_datetime='2021-12-05 00:00:30',
                                          rainfall=454,
                                          rainfall_quality=None,
                                          temperature=32,
                                          temperature_quality=None,
                                          humidity=None,
                                          humidity_quality=None,
                                          wind_direction=None,
                                          wind_direction_quality=None,
                                          wind_speed=12,
                                          wind_speed_quality=1,
                                          pressure=3,
                                          pressure_quality=43,
                                          solar_radiation=None,
                                          solar_radiation_quality=None,
                                          station="231828A",
                                          )
        SensorData.objects.create(sensor_datetime='2021-12-31 15:00:30',
                                          rainfall=12,
                                          rainfall_quality=None,
                                          temperature=24,
                                          temperature_quality=None,
                                          humidity=None,
                                          humidity_quality=None,
                                          wind_direction=None,
                                          wind_direction_quality=None,
                                          wind_speed=5,
                                          wind_speed_quality=1,
                                          pressure=5,
                                          pressure_quality=4,
                                          solar_radiation=None,
                                          solar_radiation_quality=3,
                                          station="231827A"
                                          )



    def test_download(self):
        response = self.client.get(self.download_url)
        print(response.content)
        respected_result = b'id,sensor_datetime,rainfall,rainfall_quality,temperature,temperature_quality,humidity,humidity_quality,wind_direction,wind_direction_quality,wind_speed,wind_speed_quality,pressure,pressure_quality,solar_radiation,solar_radiation_quality,station\r\n4,2021-12-05 00:00:30+00:00,454.0,,32.0,,,,,,12.00,1,3.0,43,,,231828A\r\n5,2021-12-31 15:00:30+00:00,12.0,,24.0,,,,,,5.00,1,5.0,4,,3,231827A\r\n'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), HttpResponse)
        self.assertEqual(response.content, respected_result)
        print("Download success")




>>>>>>> f5ed34c7edf7bad9c8b800dfd3907b13663ddc02





