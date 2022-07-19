from django.urls import path
from .views import SensorsInfo, SensorsPatch,MeasurementsPost
urlpatterns = [
    path('sensors/', SensorsInfo.as_view()),
    path('sensors/<pk>', SensorsPatch.as_view()),
    path('sensors/measurements/', MeasurementsPost.as_view()),
]