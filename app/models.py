from django.db import models


class SensorData(models.Model):
    """
        This class is used to declare the structure of the database.
        In theis class, there are 16 fields. The first fields named "id" that is the number of the data.
        Other fields are the fields from the client data file.
        These fields are the different columns in their database.
    """
    id = models.AutoField(verbose_name='id', primary_key=True)
    sensor_datetime = models.DateTimeField(verbose_name='sensor_datetime')
    rainfall = models.DecimalField(verbose_name='rainfall', max_digits=20, decimal_places=1, null=True)
    rainfall_quality = models.IntegerField(verbose_name='rainfall_quality', null=True)
    temperature = models.DecimalField(verbose_name='temperature', max_digits=20, decimal_places=1, null=True)
    temperature_quality = models.IntegerField(verbose_name='temperature_quality', null=True)
    humidity = models.DecimalField(verbose_name='humidity', max_digits=20, decimal_places=1, null=True)
    humidity_quality = models.IntegerField(verbose_name='humidity_quality', null=True)
    wind_direction = models.IntegerField(verbose_name='wind_direction', null=True)
    wind_direction_quality = models.IntegerField(verbose_name='wind_direction_quality', null=True)
    wind_speed = models.DecimalField(verbose_name='wind_speed', max_digits=20, decimal_places=2, null=True)
    wind_speed_quality = models.IntegerField(verbose_name='wind_speed_quality', null=True)
    pressure = models.DecimalField(verbose_name='pressure', max_digits=20, decimal_places=1, null=True)
    pressure_quality = models.IntegerField(verbose_name='pressure_quality', null=True)
    solar_radiation = models.DecimalField(verbose_name='solar_radiation', max_digits=20, decimal_places=1, null=True)
    solar_radiation_quality = models.IntegerField(verbose_name='solar_radiation_quality', null=True)
    station = models.CharField(verbose_name='station', max_length=255)

