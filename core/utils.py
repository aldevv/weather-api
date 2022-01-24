from datetime import datetime
from django.views.decorators.cache import cache_page


def toFahrenheit(kelvin: float) -> float:
    return round(kelvin * 1.8 - 459.67, 2)


def toCelcius(kelvin: float) -> float:
    return round(kelvin - 273.15, 2)


def kmhToMph(kmh: float) -> float:
    return 0.6214 * kmh


def unixTimeToHumanTime(unixtime: int) -> str:
    return datetime.utcfromtimestamp(unixtime).strftime("%H:%M")


def unixTimeToHumanDate(unixtime: int) -> str:
    return datetime.utcfromtimestamp(unixtime).strftime("%Y-%m-%d %H:%M:%S")


def getWindStrength(speed: float, mph=False) -> str:
    if not mph:
        speed = kmhToMph(speed)

    if speed < 1:
        return "calm"
    if speed >= 1 and speed <= 3:
        return "Light Air"
    if speed >= 4 and speed <= 7:
        return "Light Breeze"
    if speed >= 8 and speed <= 12:
        return "Gentle Breeze"
    if speed >= 13 and speed <= 18:
        return "Moderate Breeze"
    if speed >= 19 and speed <= 24:
        return "Fresh Breeze"
    if speed >= 25 and speed <= 31:
        return "Strong Breeze"
    if speed >= 32 and speed <= 38:
        return "Near Gale"
    if speed >= 39 and speed <= 46:
        return "Gale"
    if speed >= 47 and speed <= 54:
        return "Strong Gale"
    if speed >= 55 and speed <= 63:
        return "Whole Gale"
    if speed >= 64 and speed <= 75:
        return "Storm Force"
    if speed >= 75:
        return "Storm Force"
    return ""


def degToCardinal(deg: int) -> str:
    dirs = [
        "north",
        "north-northeast",
        "northeast",
        "east-northeast",
        "east",
        "east-southeast",
        "southeast",
        "south-southeast",
        "south",
        "south-southwest",
        "southwest",
        "west-southwest",
        "west",
        "west-northwest",
        "northwest",
        "north-northwest",
    ]
    ix = round(deg / (360.0 / len(dirs)))
    return dirs[ix % len(dirs)]
