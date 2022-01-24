from rest_framework.response import Response
from rest_framework.views import APIView
import requests as requests
from core.serializers import WeatherQueryParamsSerializer, WeatherResponseSerializer
from weather.settings import EXTERNAL_API as URL
from weather.settings import EXTERNAL_API_KEY as apikey
from core.utils import (
    toCelcius,
    degToCardinal,
    getWindStrength,
    toFahrenheit,
    unixTimeToHumanTime,
    unixTimeToHumanDate,
)

from rest_framework import status
from django.core.cache import cache
import hashlib

# Create your views here.


class WeatherAPI(APIView):
    def get(self, req):
        qp = WeatherQueryParamsSerializer(data=req.query_params)
        qp.is_valid(raise_exception=True)

        cache_key = hashlib.md5(
            bytes("".join(qp.data.values()), encoding="utf-8")
        ).hexdigest()
        if payload := cache.get(cache_key):
            return Response(
                payload, status=status.HTTP_200_OK, content_type="application/json"
            )

        qp = {"q": ",".join(qp.data.values())}
        qp = qp | {"appid": apikey}
        res = requests.get(URL, params=qp).json()
        res = WeatherResponseSerializer(data=res)
        res.is_valid(raise_exception=True)
        res = res.data

        payload = {
            "location_name": f"{res['name']}, {res['sys']['country']}",
            "temperature_celcius": f"{toCelcius(float(res['main']['temp']))} ºC",
            "temperature_fahrenheit": f"{toFahrenheit(float(res['main']['temp']))} ºF",
            "wind": f"{getWindStrength(float(res['wind']['speed']))}, {res['wind']['speed']} m/s, {degToCardinal(int(res['wind']['deg']))}",
            "cloudiness": f"{res['weather'][0]['description']}",
            "preasure": f"{res['main']['pressure']} hpa",
            "humidity": f"{res['main']['humidity']}%",
            "sunrise": f"{unixTimeToHumanTime(int(res['sys']['sunrise']))}",
            "sunset": f"{unixTimeToHumanTime(int(res['sys']['sunset']))}",
            "geo_coordinates": f"[{round(float(res['coord']['lat']), 2)}, {round(float(res['coord']['lon']), 2)}]",
            "requested_time": f"{unixTimeToHumanDate(int(res['dt']))}",
        }

        cache.set(cache_key, payload)

        return Response(
            payload, status=status.HTTP_200_OK, content_type="application/json"
        )
