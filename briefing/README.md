# Morning Briefing CLI

An async Python CLI application that generates a clean morning briefing with:

- FX exchange rates
- Weather reports for multiple cities
- Top tech news headlines

The application fetches data concurrently from multiple APIs, validates responses with Pydantic, caches results for 10 minutes, and renders a professional terminal dashboard in under 3 seconds.

---

## 🔥 Features

- Async concurrent API fetching using `asyncio` + `httpx`
- 10-minute `diskcache`-backed cache with automatic TTL expiration
- Graceful degradation when APIs fail
- Pydantic validation for every API response
- Dataclass-based domain models
- Environment-variable based API key management
- Human-readable CLI output
- Optional machine-readable JSON output
- Scheduled automation via cron or Task Scheduler
- Optional email delivery
- Modular layered architecture

---

## 💻 Example Output

```text
=== MORNING BRIEFING — Fri, 29 May 2026, 15:12 ===

WEATHER
Mumbai      33°C  mainly clear
Bangalore   32°C  clear
Delhi       35°C  partly cloudy

TOP TECH NEWS
1. Claude Opus 4.8
2. Bricks and Minifigs Stole a Man's $200k Lego Collection
3. Volkswagen blocks Home Assistant by requiring client assertion
4. I made a million dollar product from my dorm room (2025)
5. Claude Code – Everything You Can Configure That the Docs Don't Tell You

FX
USD/INR     95.78
USD/EUR     0.86


Completed in 0.05s
```

---

## 🧠 Tech Stack

- Python 3.12+
- `asyncio`
- `httpx`
- `Pydantic`
- `python-dotenv`
- `diskcache`

**APIs used:**

- Open-Meteo (weather)
- Hacker News API (tech news)
- ExchangeRate API (FX rates)

---

## 📂 Project Structure

```
briefing/
│
├── .env
├── requirements.txt
├── README.md
│
├── cache/
│
└── briefing/
    ├── main.py
    ├── fetchers.py
    ├── models.py
    ├── schemas.py
    ├── emailer.py
    ├── cache.py
    ├── display.py
    ├── config.py
    └── utils.py
```

---

## ⚙️ Setup

### 1. Clone Repository

```bash
git clone https://github.com/BhaumikLuhar/mini-python-projects.git
cd briefing
```

### 2. Create Virtual Environment

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

```env
FX_API_KEY=your_api_key_here
```

Get a free API key from: https://www.exchangerate-api.com

---

## 🚀 Usage

**Run the briefing:**

```bash
python -m briefing.main
```

**Run with JSON output:**

```bash
python -m briefing.main --json
```

---

## 🏗️ Architecture

The application uses a layered architecture:

| Layer          | Module        | Responsibility                                      |
|----------------|---------------|-----------------------------------------------------|
| Fetch          | `fetchers.py` | Async HTTP requests and API communication           |
| Validation     | `schemas.py`  | Pydantic models validate all incoming API responses |
| Domain         | `models.py`   | Dataclasses represent clean internal business objects |
| Cache          | `cache.py`    | Filesystem-based cache with 10-minute TTL           |
| Display        | `display.py`  | Terminal formatting and rendering                   |
| Configuration  | `config.py`   | Environment variable and settings management        |
| Utilities      | `utils.py`    | Shared helper functions                             |

This separation of concerns keeps the project modular, testable, and maintainable.

---

## ⚡ Why Async?

The application fetches weather, FX, and news concurrently using `asyncio.gather()`.

| Mode           | Runtime                          |
|----------------|----------------------------------|
| Without async  | Sum of all individual request times |
| With async     | Slowest single request only      |

This keeps fresh-cache execution under 3 seconds.

---

## 🗃️ Caching

The project uses the `diskcache` library for all API response caching.

**Benefits:**

- Automatic TTL expiration
- Safer serialization
- Improved reliability
- Simpler implementation
- Faster reruns
- Reduced API usage
- Lower chance of hitting rate limits

Cache files are stored in:

```
cache/
```

---

## ⏰ Scheduled Automation

The application can be scheduled to run automatically every morning.

**Linux/macOS — cron:**

```bash
0 8 * * * cd /path/to/briefing && python -m briefing.main --email
```

**Windows — Task Scheduler:**

Create a new basic task pointing to:

```
python -m briefing.main
```

Set the trigger to run daily at your preferred time.

Optional email delivery is supported for receiving the briefing directly in your inbox.

---

## 🛡️ Graceful Degradation

If one API fails:

- Remaining services still render successfully
- Clear warnings are displayed
- Application does not crash

This improves resilience and user experience.

---

## 🎓 Concepts Demonstrated

This project demonstrates:

- Async programming
- Concurrent I/O
- HTTP APIs
- Defensive programming
- Pydantic validation
- Dataclasses
- Filesystem caching
- Environment variable management
- CLI application design
- Layered architecture
- Graceful degradation

---

## 📈 Future Improvements

Potential enhancements:

- Rich terminal formatting
- Retry logic with exponential backoff
- Docker packaging
- Unit/integration tests
- Logging system
- SQLite persistence