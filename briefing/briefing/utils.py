from datetime import datetime


WEATHER_CODES = {
    0: "clear",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "depositing rime fog",
    51: "light drizzle",
    53: "moderate drizzle",
    55: "dense drizzle",
    61: "slight rain",
    63: "moderate rain",
    65: "heavy rain",
    80: "rain showers",
    95: "thunderstorm",
}


def weather_description(code: int) -> str:
    return WEATHER_CODES.get(code, "unknown")

def log_cache_hit(name: str) -> None:
    print(f"[CACHE HIT] {name}")


def log_cache_miss(name: str) -> None:
    print(f"[CACHE MISS] {name}")

#HackerNews returns: Unix timestamps
def unix_to_datetime(
    timestamp: int,
) -> datetime:

    return datetime.fromtimestamp(timestamp)


def current_timestamp() -> str:
    return datetime.now().strftime(
        "%a, %d %b %Y, %H:%M"
    )