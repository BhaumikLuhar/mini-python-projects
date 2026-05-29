from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

CACHE_DIR = BASE_DIR / "cache"

CACHE_TTL_SECONDS = 600

REQUEST_TIMEOUT = 10


CITIES = {
    "Mumbai": {
        "latitude": 19.07,
        "longitude": 72.87,
    },
    "Bangalore": {
        "latitude": 12.97,
        "longitude": 77.59,
    },
    "Delhi": {
        "latitude": 28.61,
        "longitude": 77.20,
    },
}