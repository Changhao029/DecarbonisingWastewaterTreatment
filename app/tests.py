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
        self.data_query_all_url = '/datatable/?page=1'
        self.data_query_one_url = '/datatable/?station=231825A'
        self.data_query_none_url = '/datatable/?station=23'
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

    def test_data_query_all(self):
        c = Client()
        response = c.get(self.data_query_all_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], len(SensorData.objects.all()))
        print("Query all data successfully")

    def test_data_query_one(self):
        c = Client()
        response = c.get(self.data_query_one_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["results"][0]["station"], "231825A")
        print("Query one piece of data with condition successfully")

    def test_data_query_none(self):
        c = Client()
        response = c.get(self.data_query_none_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 0)
        print("Get correct response successfully when query one")


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
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231826A",
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
        print("Query all data in Line Chart successfully")


class BarChartTest(TestCase):
    def setUp(self):
        self.line_chart_url = '/Barchart/'
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
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231826A",
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
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231827A",
                                  )
    def test_barchart(self):
        c = Client()
        response = c.get('/barchart/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.data, dict))
        self.assertTrue('rainfall' in response.data)
        self.assertTrue('humidity' in response.data)
        self.assertTrue(isinstance(response.data['rainfall'], list))
        self.assertTrue(isinstance(response.data['humidity'], list))
        self.assertEqual(len(response.data['humidity']), len(response.data['rainfall']))
        print("Query all data in Bar Chart successfully")




from django.http.response import HttpResponse
class DownloadTest(TestCase):
    """
    Test view for Download data as csv file function.
    """
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
        # count the number of \n in response content
        line_count = response.content.count(b'\x0a')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), HttpResponse)
        self.assertEqual(line_count, 3)
        print("Download data file successfully")
