from rest_framework import serializers


class WeatherQueryParamsSerializer(serializers.Serializer):
    city = serializers.CharField(required=False)
    country = serializers.CharField(required=False)


class CoordinatesSerializer(serializers.Serializer):
    lon = serializers.CharField()
    lat = serializers.CharField()


class CountrySerializer(serializers.Serializer):
    country = serializers.CharField()
    sunrise = serializers.CharField()
    sunset = serializers.CharField()


class MainSerializer(serializers.Serializer):
    pressure = serializers.CharField()
    humidity = serializers.CharField()
    temp = serializers.CharField()


class WindSerializer(serializers.Serializer):
    speed = serializers.CharField()
    deg = serializers.CharField()


class WeatherSerializer(serializers.Serializer):
    description = serializers.CharField()


class WeatherResponseSerializer(serializers.Serializer):
    weather = serializers.ListField(child=WeatherSerializer())
    sys = CountrySerializer()
    coord = CoordinatesSerializer()
    main = MainSerializer()
    wind = WindSerializer()
    name = serializers.CharField()
    dt = serializers.CharField()
