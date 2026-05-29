from briefing.cache import (
    load_cache,
    save_cache,
)
from briefing.config import CACHE_TTL_SECONDS


def main() -> None:

    cached = load_cache(
        "test",
        CACHE_TTL_SECONDS,
    )

    if cached:
        print("Loaded from cache:")
        print(cached)

    else:
        print("No valid cache found")

        data = {
            "message": "hello world"
        }

        save_cache("test", data)

        print("Saved new cache")


if __name__ == "__main__":
    main()