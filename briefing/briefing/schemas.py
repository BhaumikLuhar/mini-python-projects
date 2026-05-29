from pydantic import BaseModel
from typing import Any

class CurrentWeatherSchema(BaseModel):
    temperature_2m: float
    weather_code: int

class WeatherResponseSchema(BaseModel):
    current: CurrentWeatherSchema

class HackerNewsStorySchema(BaseModel):
    title: str
    url: str | None = None
    by: str
    time: int

class FxRatesSchema(BaseModel):
    conversion_rates: dict[str, float]


class FxResponseSchema(BaseModel):
    base_code: str
    conversion_rates: dict[str, float]