from app.models import SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["id", "sensor_datetime", "rainfall", "temperature", "humidity", "wind_direction", "wind_speed", "pressure", "solar_radiation", "station"]


class FakeSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = "__all__"


class LineChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "sensor_datetime", "temperature", "wind_speed", "pressure", "solar_radiation"]


class TemperatureLineChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "sensor_datetime", "temperature"]


class WindSpeedLineChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "sensor_datetime", "wind_speed"]


class PressureLineChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "sensor_datetime", "pressure"]


class SolarRadiationLineChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "sensor_datetime", "solar_radiation"]


class WindRoseChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "wind_direction", "wind_speed"]


class BarChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ["rainfall", "humidity","sensor_datetime"]