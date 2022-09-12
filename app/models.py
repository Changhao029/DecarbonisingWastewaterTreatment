from django.db import models


class SensorData(models.Model):
    """

    """
    station_choices = (
        (1, "231824A"),
        (2, "231825A"),
        (3, "231826A"),
        (4, "231827A"),
        (5, "231828A")
    )
    id = models.AutoField(verbose_name='id', primary_key=True)
    sensor_datetime = models.DateTimeField(verbose_name='sensor_datetime')
    rainfall = models.DecimalField(verbose_name='rainfall', max_digits=20, decimal_places=1, null=True)
    rainfall_quality = models.IntegerField(verbose_name='rainfall_quality', null=True)
    temperature = models.DecimalField(verbose_name='temperature', max_digits=20, decimal_places=1, null=True)
    temperature_quality = models.IntegerField(verbose_name='temperature_quality', null=True)
    humidity = models.DecimalField(verbose_name='humidity', max_digits=20, decimal_places=1)
    humidity_quality = models.IntegerField(verbose_name='humidity_quality')
    wind_direction = models.IntegerField(verbose_name='wind_direction')
    wind_direction_quality = models.IntegerField(verbose_name='wind_direction_quality')
    wind_speed = models.DecimalField(verbose_name='wind_speed', max_digits=20, decimal_places=2)
    wind_speed_quality = models.IntegerField(verbose_name='wind_speed_quality')
    pressure = models.DecimalField(verbose_name='pressure', max_digits=20, decimal_places=1, null=True)
    pressure_quality = models.IntegerField(verbose_name='pressure_quality', null=True)
    solar_radiation = models.DecimalField(verbose_name='solar_radiation', max_digits=20, decimal_places=1, null=True)
    solar_radiation_quality = models.IntegerField(verbose_name='solar_radiation_quality', null=True)
    station = models.IntegerField(verbose_name='station', choices=station_choices, default=1)

