from rest_framework import serializers


class WeatherQueryParamsSerializer(serializers.Serializer):
    city = serializers.CharField(required=False)
    country = serializers.CharField(required=False)


class CountrySerializer(serializers.Serializer):
    country = serializers.CharField()


class WeatherResponseSerializer(serializers.Serializer):
    sys = CountrySerializer()
    name = serializers.CharField()
