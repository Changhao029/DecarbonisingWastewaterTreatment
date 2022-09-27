from app.models import SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = "__all__"


class FakeSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = "__all__"


class LineChartDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = ["station", "sensor_datetime", "temperature", "wind_speed", "pressure", "solar_radiation"]


class BarChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ["rainfall", "humidity", "sensor_datetime"]