from dataclasses import dataclass
from datetime import datetime

@dataclass
class FxRate:
    from_currency: str
    to_currency: str
    rate: float
    change: float
    fetched_at: datetime


@dataclass
class WeatherReport:
    city: str
    temp_c: float
    conditions: str
    rain_chance: int


@dataclass
class NewsItem:
    title: str
    url: str
    source: str
    published: datetime