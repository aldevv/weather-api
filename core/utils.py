from datetime import datetime


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


def getWindStrength(kmh: float, mph=False) -> str:
    if not mph:
        mph = kmhToMph(kmh)

    if mph < 1:
        return "calm"
    if mph >= 1 and mph <= 3:
        return "Light Air"
    if mph >= 4 and mph <= 7:
        return "Light Breeze"
    if mph >= 8 and mph <= 12:
        return "Gentle Breeze"
    if mph >= 13 and mph <= 18:
        return "Moderate Breeze"
    if mph >= 19 and mph <= 24:
        return "Fresh Breeze"
    if mph >= 25 and mph <= 31:
        return "Strong Breeze"
    if mph >= 32 and mph <= 38:
        return "Near Gale"
    if mph >= 39 and mph <= 46:
        return "Gale"
    if mph >= 47 and mph <= 54:
        return "Strong Gale"
    if mph >= 55 and mph <= 63:
        return "Whole Gale"
    if mph >= 64 and mph <= 75:
        return "Storm Force"
    if mph >= 75:
        return "Storm Force"
    return ""


def degToCardinal(deg: int):
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
