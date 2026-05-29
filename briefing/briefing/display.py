from collections.abc import Sequence
from datetime import datetime

from briefing.models import (
    FxRate,
    NewsItem,
    WeatherReport,
)

def render_header() -> None:

    now = datetime.now().strftime(
        "%a, %d %b %Y, %H:%M"
    )

    print()
    print(
        f"=== MORNING BRIEFING — {now} ==="
    )
    print()


def render_fx(rates: Sequence[FxRate])-> None:

    print("FX")

    if not rates:
        print("FX data unavailable")
        print()
        return
    
    for rate in rates:
        pair = (
            f"{rate.from_currency}/"
            f"{rate.to_currency}"
        )

        print(
            f"{pair:<12}"
            f"{rate.rate:.2f}"
        )

    print()


def render_weather(
    reports: Sequence[WeatherReport],
) -> None:

    print("WEATHER")

    if not reports:
        print(
            "Weather data unavailable"
        )
        print()
        return

    for report in reports:

        print(
            f"{report.city:<12}"
            f"{report.temp_c:.0f}°C  "
            f"{report.conditions}"
        )

    print()


def render_news(
    items: Sequence[NewsItem],
) -> None:

    print("TOP TECH NEWS")

    if not items:
        print("News unavailable")
        print()
        return

    for index, item in enumerate(
        items,
        start=1,
    ):

        print(
            f"{index}. {item.title}"
        )

    print()


def render_warning(service: str, error: Exception,)->None:
    print(
        f"{service} failed: "
        f"{type(error).__name__}"
    )