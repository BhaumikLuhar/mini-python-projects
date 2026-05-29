import os
import httpx

from briefing.cache import (
    load_cache,
    save_cache,
)
from briefing.config import (
    CACHE_TTL_SECONDS,
    CITIES,
    REQUEST_TIMEOUT,
)
from briefing.models import (
    FxRate,
    NewsItem,
    WeatherReport,
)
from briefing.schemas import (
    FxResponseSchema,
    HackerNewsStorySchema,
    WeatherResponseSchema,
)
from briefing.utils import (
    weather_description,
    unix_to_datetime,
)


async def fetch_weather(client: httpx.AsyncClient,)->list[WeatherReport]:
    cache_name="weather"

    cached=load_cache(cache_name,CACHE_TTL_SECONDS)

    if cached:
        reports=[]
        for report in cached:
            reports.append(WeatherReport(**report))

        return reports
    
    reports=[]

    for city, coords in CITIES.items():
        url = (
            "https://api.open-meteo.com/v1/forecast"
        )

        params = {
            "latitude": coords["latitude"],
            "longitude": coords["longitude"],
            "current": (
                "temperature_2m,weather_code"
            ),
            "hourly": "precipitation_probability",
            "forecast_days": 1,
        }

        response= await client.get(url,params=params,timeout=REQUEST_TIMEOUT)

        response.raise_for_status()

        validated=(WeatherResponseSchema.model_validate(response.json()))

        current=validated.current

        report=WeatherReport(
            city=city,
            temp_c=current.temperature_2m,
            conditions=weather_description(current.weather_code),
            rain_chance=0,
        )

        reports.append(report)

    save_cache(cache_name,[r.__dict__ for r in reports])

    return reports

async def fetch_fx(client: httpx.AsyncClient,)->list[FxRate]:

    cache_name="fx"

    cached=load_cache(cache_name,CACHE_TTL_SECONDS)

    if cached:
        rates=[]

        for item in rates:
            rates.append(FxRate(**item))

        return rates
    
    api_key=os.getenv("FX_API_KEY")

    if not api_key:
        raise ValueError(
            "FX_API_KEY missing in .env"
        )

    url = (
        f"https://v6.exchangerate-api.com/"
        f"v6/{api_key}/latest/USD"
    )

    response = await client.get(url,timeout=REQUEST_TIMEOUT)

    response.raise_for_status()

    validated=(FxResponseSchema.model_validate(response.json()))

    rates=[]

    currencies = ["INR", "EUR"]

    for currency in currencies:

        rate = validated.conversion_rates[
            currency
        ]

        fx = FxRate(
            from_currency="USD",
            to_currency=currency,
            rate=rate,
            change=0.0,
            fetched_at=unix_to_datetime(0),
        )

        rates.append(fx)

    rates=[item.to_dict() for item in rates]
    save_cache(
        cache_name,
        rates,
    )

    return rates


async def fetch_news(
    client: httpx.AsyncClient,
) -> list[NewsItem]:

    cache_name = "news"

    cached = load_cache(
        cache_name,
        CACHE_TTL_SECONDS,
    )

    if cached:

        items = []

        for item in cached:

            items.append(
                NewsItem(**item)
            )

        return items

    top_stories_url = (
        "https://hacker-news.firebaseio.com/"
        "v0/topstories.json"
    )

    response = await client.get(
        top_stories_url,
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    story_ids = response.json()[:5]

    items = []

    for story_id in story_ids:

        story_url = (
            "https://hacker-news.firebaseio.com/"
            f"v0/item/{story_id}.json"
        )

        story_response=await client.get(story_url,timeout=REQUEST_TIMEOUT)

        story_response.raise_for_status()

        validated=(HackerNewsStorySchema.model_validate(story_response.json()))

        news = NewsItem(
            title=validated.title,
            url=validated.url or "",
            source="HackerNews",
            published=unix_to_datetime(
                validated.time
            ),
        )

        items.append(news)

    items=[item.to_dict() for item in items]
    save_cache(cache_name,items)

    return items


