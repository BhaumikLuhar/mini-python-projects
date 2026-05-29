from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

CACHE_DIR = BASE_DIR / "cache"

CACHE_TTL_SECONDS = 60

REQUEST_TIMEOUT = 10

load_dotenv(BASE_DIR / ".env")


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