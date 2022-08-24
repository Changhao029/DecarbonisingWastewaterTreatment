import json

from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import SensorData
from app.serializers import SensorDataSerializer


class DataTable(APIView):

    def get(self, *args, **kwargs):

        if kwargs.get("station"):
            queryset = SensorData.objects.filter(station=kwargs.get("station"))
        else:
            queryset = SensorData.objects.all()
        ser = SensorDataSerializer(instance=queryset, many=True)
        return Response({"result": ser.data})


class FakeData(APIView):

    def post(self, *args, **kwargs):
        return Response("fakedata")