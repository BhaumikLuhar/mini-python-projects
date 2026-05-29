import asyncio
from email import parser
import time
import httpx
import argparse
import json

from briefing.display import (
    render_fx,
    render_header,
    render_news,
    render_warning,
    render_weather,
)
from briefing.fetchers import (
    fetch_fx,
    fetch_news,
    fetch_weather,
)


async def fetch_briefing():

    async with httpx.AsyncClient(verify=False) as client:

        weather, news, fx = (
            await asyncio.gather(
                fetch_weather(client),
                fetch_news(client),
                fetch_fx(client),
                return_exceptions=True,
            )
        )

    return {
        "weather": weather,
        "news": news,
        "fx": fx,
    }


def main() -> None:
    start = time.perf_counter()
    briefing = asyncio.run(
        fetch_briefing()
    )

    render_header()

    weather = briefing["weather"]

    if isinstance(weather, Exception):
        render_warning(
            "Weather",
            weather,
        )
        render_weather([])
    else:
        render_weather(weather)

    news = briefing["news"]

    if isinstance(news, Exception):
        render_warning(
            "News",
            news,
        )
        render_news([])
    else:
        render_news(news)

    fx = briefing["fx"]

    if isinstance(fx, Exception):
        render_warning(
            "FX",
            fx,
        )
        render_fx([])
    else:
        render_fx(fx)


    parser = argparse.ArgumentParser()

    parser.add_argument(
    "--json",
    action="store_true",
)

    args = parser.parse_args()
    if args.json:

        print(
        json.dumps(
            briefing,
            indent=4,
            default=str,
            )
        )


    elapsed = (
    time.perf_counter() - start
    )

    print(
        f"Completed in "
        f"{elapsed:.2f}s"
    )


if __name__ == "__main__":
    main()