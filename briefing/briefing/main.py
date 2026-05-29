import asyncio
import time
import httpx
import argparse
import json
from briefing.emailer import send_email
from briefing.display import (
    render_fx,
    render_header,
    render_news,
    render_warning,
    render_weather,
)
from io import StringIO
import contextlib
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
    buffer = StringIO()
    with contextlib.redirect_stdout(
    buffer
    ):

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
    parser.add_argument(
    "--email",
    action="store_true",
    )
    
    output = buffer.getvalue()
    print(output)

    
    args = parser.parse_args()
    if args.json:

        print(
        json.dumps(
            briefing,
            indent=4,
            default=str,
            )
        )

    if args.email:

        send_email(
        subject="Morning Briefing",
        body=output,
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