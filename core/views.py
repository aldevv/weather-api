from rest_framework.response import Response
from rest_framework.views import APIView
import requests as requests
from core.serializers import WeatherQueryParamsSerializer, WeatherResponseSerializer
from weather.settings import EXTERNAL_API as URL
from weather.settings import EXTERNAL_API_KEY as key
from core.utils import (
    toCelcius,
    degToCardinal,
    getWindStrength,
    toFahrenheit,
    unixTimeToHumanTime,
    unixTimeToHumanDate,
)

from rest_framework import status

# Create your views here.


class WeatherAPI(APIView):
    def get(self, req):
        qp = WeatherQueryParamsSerializer(data=req.query_params)
        qp.is_valid(raise_exception=True)
        qp = {"q": ",".join(qp.data.values())}
        qp = qp | {"appid": key}
        res = requests.get(URL, params=qp).json()
        data = WeatherResponseSerializer(data=res)
        data.is_valid(raise_exception=True)

        payload = {
            "location_name": f"{res['name']}, {res['sys']['country']}",
            "temperature_celcius": toCelcius(float(res["main"]["temp"])),
            "temperature_fahrenheit": toFahrenheit(float(res["main"]["temp"])),
            "wind": f"{getWindStrength(res['wind']['speed'])}, {res['wind']['speed']} m/s, {degToCardinal(res['wind']['deg'])}",
            "cloudiness": f"{res['weather'][0]['description']}",
            "preasure": f"{res['main']['pressure']} hpa",
            "humidity": f"{res['main']['humidity']}%",
            "sunrise": f"{unixTimeToHumanTime(int(res['sys']['sunrise']))}",
            "sunset": f"{unixTimeToHumanTime(int(res['sys']['sunset']))}",
            "geo_coordinates": f"[{res['coord']['lat']}, {res['coord']['lon']}]",
            "requested_time": f"{unixTimeToHumanDate(int(res['dt']))}",
        }

        return Response(
            payload, status=status.HTTP_200_OK, content_type="application/json"
        )
