from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensors(models.Model):

    name = models.CharField(max_length=10)
    description = models.TextField(max_length=50)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)