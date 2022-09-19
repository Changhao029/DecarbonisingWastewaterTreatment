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
        self.base_url = '/datatable/?page=1'
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
                                  pressure=None,
                                  pressure_quality=None,
                                  solar_radiation=None,
                                  solar_radiation_quality=None,
                                  station="231826A",
                                  )

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





