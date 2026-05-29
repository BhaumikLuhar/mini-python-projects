import asyncio

import httpx

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

    briefing = asyncio.run(
        fetch_briefing()
    )

    print(briefing)


if __name__ == "__main__":
    main()