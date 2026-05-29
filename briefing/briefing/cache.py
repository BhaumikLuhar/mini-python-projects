from typing import Any

from diskcache import Cache

from briefing.config import (
    CACHE_DIR,
    CACHE_TTL_SECONDS,
)


cache = Cache(CACHE_DIR)


def load_cache(
    key: str,
) -> Any | None:

    return cache.get(key)


def save_cache(
    key: str,
    value: Any,
    ttl: int = CACHE_TTL_SECONDS,
) -> None:

    cache.set(
        key,
        value,
        expire=ttl,
    )