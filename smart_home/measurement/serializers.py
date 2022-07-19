from rest_framework import serializers
from .models import Sensors,Measurement

# TODO: опишите необходимые сериализаторы

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

class SensorsSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True,many=True)
    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description', 'measurements']