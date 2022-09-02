from app.models import SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):
    station_num = serializers.SerializerMethodField()

    def get_station_num(self, obj):
        return obj.get_station_display()

    class Meta:
        model = SensorData
        fields = "__all__"


class FakeSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = "__all__"


class LineChartDataSerializer(serializers.ModelSerializer):
    station_num = serializers.SerializerMethodField()

    def get_station_num(self, obj):
        return obj.get_station_display()

    class Meta:
        model = SensorData
        fields = ["station_num", "sensor_datetime", "temperature", "wind_speed", "pressure", "solar_radiation"]