from django.urls import path
from core.views import WeatherAPI

urlpatterns = [path("weather/", WeatherAPI.as_view(), name="weather")]
