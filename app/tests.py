import os,django

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


class BaseTest(TestCase):
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

    def test_query_all(self):
        c = Client()
        response = c.get(self.base_url)
        print(response.data)
        self.assertEqual(response.status_code,200)




