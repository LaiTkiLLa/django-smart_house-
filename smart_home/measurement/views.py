# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView

from .models import Sensors, Measurement
from .serializers import SensorsSerializer, MeasurementSerializer
from rest_framework.response import Response

class SensorsInfo(APIView):

    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    def get(self, request):
        sensors = Sensors.objects.all()
        ser = SensorsSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        serializer = SensorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'status': 'OK'})

class SensorsPatch(RetrieveAPIView):

    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer

    def patch(self, request, pk):
        sensor = Sensors.objects.get(pk=pk)
        serializer = SensorsSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class MeasurementsPost(APIView):

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def get(self, request):
        measurement = Measurement.objects.all()
        mer = MeasurementSerializer(measurement, many=True)
        return Response(mer.data)

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'status': 'OK'})