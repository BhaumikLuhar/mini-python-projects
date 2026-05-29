from dataclasses import dataclass
from datetime import datetime

@dataclass
class FxRate:
    from_currency: str
    to_currency: str
    rate: float
    change: float
    fetched_at: datetime

    def to_dict(self):
        return {
            "from_currency": self.from_currency,
            "to_currency": self.to_currency,
            "rate": self.rate,
            "change": self.change,
            "fetched_at": self.fetched_at.isoformat()
        }


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

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "published": self.published.isoformat()
        }