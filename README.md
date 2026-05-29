# 🐍 mini-python-projects

A collection of Python CLI tools built to automate real day-to-day workflows. Each project is independently runnable, professionally structured, and solves a concrete business problem.

> Estimated impact: saves 5–30 minutes per task. Across a team of 5, that's **80+ hours recovered monthly**.

---

## 📁 Projects

---

### 1. 🛠️ Toolkit CLI

A multi-purpose CLI that handles 10 common utility tasks in one place — GST calculation, currency conversion, age calculation, employee ID generation, file renaming, slug generation, batch rename, password generation, QR code export, and command history logging.

**Business problem:** Small repetitive tasks like GST breakdowns, file renames, and currency lookups consume 3–5 minutes each. At 10 uses/day across a team, that's 80+ hours lost monthly to tasks that should take seconds.

**Key commands:**

```bash
python toolkit.py gst 5000 luxury           # GST breakdown with CGST/SGST
python toolkit.py convert 100 USD INR       # Currency conversion
python toolkit.py password 16 --symbols     # Secure password generator
python toolkit.py batchrename report invoice --preview  # Bulk rename with preview
python toolkit.py qr "https://google.com" --output google_qr
```

**Stack:** Python 3, `argparse`, `os`, `datetime`, `random`, `qrcode`

📂 [`/Toolkit`](./Toolkit)

---

### 2. 📊 Expense Consolidator

An ETL pipeline that ingests messy expense CSVs from multiple teams, normalizes inconsistent column names, auto-categorizes vendors, detects duplicates, and exports clean reports in under 5 seconds.

**Business problem:** Finance teams receive expense data from different departments with inconsistent formats — different column names (`Amount`, `AMT`, `amount`), missing categories, blank rows, and duplicates. Manual cleanup takes 20–30 minutes per dataset and introduces errors. Across a team of 5, that's ~40 hours recovered monthly.

**Adding new categorization rules** requires zero code changes — just update `rules.json`:

```json
{
    "Travel": ["uber", "ola"],
    "Meals": ["swiggy", "zomato"],
    "Infrastructure": ["aws", "gcp"]
}
```

**Key commands:**

```bash
python3 consolidate.py expenses/                   # Full run
python3 consolidate.py expenses/ --month 2026-01   # Filter by month
```

**Outputs:** `consolidated.csv`, `category_summary.csv`, `duplicates.csv`

**Stack:** Python 3, `csv`, `pathlib`, `json`, `logging`, `argparse`, `rich`

📂 [`/Expense_Consolidator`](./Expense_Consolidator)

---

### 3. ☀️ Morning Briefing CLI

An async CLI that fetches live FX rates, multi-city weather, and top tech headlines concurrently from three APIs and renders a clean terminal dashboard in under 3 seconds. API responses are cached for 10 minutes via `diskcache`.

**Business problem:** Checking FX rates, weather, and news across separate tabs every morning takes 10+ minutes and breaks focus. This consolidates it into a single command — or schedules it to run automatically.

**Example output:**

```
=== MORNING BRIEFING — Fri, 29 May 2026, 08:00 ===

FX                          WEATHER
USD/INR    83.45            Mumbai   32°C  partly cloudy
USD/EUR    0.92             Delhi    38°C  clear

TOP TECH NEWS
1. OpenAI releases new model...
2. Python 3.15 proposal...

Completed in 0.82s
```

**Schedule it** to run every morning without opening a terminal:

```bash
# cron (Linux/macOS)
0 8 * * * cd /path/to/briefing && python -m briefing.main
```

**Stack:** Python 3.12+, `asyncio`, `httpx`, `Pydantic`, `diskcache`, `python-dotenv`

📂 [`/briefing`](./briefing)

---

### 4. 📝 Notes App

A local-first CLI for creating, searching, tagging, and managing markdown notes with structured frontmatter metadata. Notes are stored as plain files — no database, no account, fully offline.

**Business problem:** Meeting notes and ideas get scattered across apps. Searching them later is slow, and most tools require accounts or internet access. This stores everything locally as readable markdown files with instant full-text and fuzzy search.

**Key commands:**

```bash
python -m noteapp.main new "Q3 Planning"              # Create note
python -m noteapp.main list --tag planning            # Filter by tag
python -m noteapp.main list --last 7                  # Notes from last 7 days
python -m noteapp.main search budget                  # Full-text search
python -m noteapp.main edit 2026-05-27-q3-planning    # Open in $EDITOR
python -m noteapp.main export                         # Export all notes → HTML
```

**Stack:** Python 3, `argparse`, `pathlib`, `datetime`, `re`

📂 [`/notes-app`](./notes-app)

---

## ⚙️ Getting Started

```bash
git clone https://github.com/BhaumikLuhar/mini-python-projects.git
cd mini-python-projects
```

Each project is self-contained. Navigate into any folder and follow its own README for setup and usage instructions.

---

## 👨‍💻 Author

**Bhaumik Luhar** — Python learning portfolio focused on backend fundamentals, CLI design, and real-world automation.