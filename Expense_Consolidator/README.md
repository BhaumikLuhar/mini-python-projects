# Expense Consolidator

A professional Python-based expense consolidation and reporting tool that processes messy CSV expense files from multiple teams, normalizes inconsistent data, auto-categorizes vendors, detects malformed rows, and generates clean financial summaries.

---

## 🧩 Business Problem

Organizations often receive expense data from different teams in inconsistent formats:

- Different column names (`Amount`, `amount`, `AMT`)
- Missing categories
- Blank rows
- Malformed records
- Duplicate entries
- Vendor naming inconsistencies

Manually cleaning and consolidating this data:

- Wastes employee time
- Increases reporting errors
- Delays financial analysis

This tool automates the entire workflow.

---

## ✅ What This Tool Does

The Expense Consolidator:

- Reads all CSV files from an `expenses/` folder
- Normalizes inconsistent column names
- Removes invalid/blank rows
- Auto-fills categories using configurable JSON rules
- Consolidates all records into one clean CSV
- Generates category-wise summaries
- Detects duplicate expenses
- Identifies top expense outliers
- Prints analytics to the terminal
- Exports structured reports

---

## 🔥 Features

### CSV Consolidation

Combines multiple CSV files into a single unified dataset.

### Column Normalization

Automatically converts inconsistent headers:

| Original   | Normalized |
|------------|------------|
| `Amount`   | `amount`   |
| `AMT`      | `amount`   |
| `Vendor`   | `vendor`   |
| `CATEGORY` | `category` |

### Rule-Based Categorization

Loads category rules dynamically from `rules.json`.

**Example:**

```json
{
    "Travel": ["uber", "ola"],
    "Meals": ["swiggy", "zomato"],
    "Infrastructure": ["aws", "gcp"],
    "Shopping": ["amazon"]
}
```

No code changes required to update rules.

### Validation & Error Handling

- Skips malformed rows
- Prevents crashes from missing values
- Logs warnings instead of stopping execution

### Duplicate Detection

Flags duplicate expenses based on:

- Date
- Vendor
- Amount

### Analytics Dashboard

Prints:

- Total spend
- Top categories
- Top outliers
- Transaction summaries

### Output Reports

Generates:

- `consolidated.csv`
- `category_summary.csv`
- `duplicates.csv`

---

## 📂 Project Structure

```
Expense_Consolidator/
│
├── consolidate.py
├── rules.json
├── README.md
│
├── expenses/
│   ├── team_a.csv
│   ├── team_b.csv
│   └── team_c.csv
│
├── outputs/
│   ├── consolidated.csv
│   ├── category_summary.csv
│   └── duplicates.csv
│
│
├── logs/
│   └── warnings.log
│
└── utils/
    ├── loader.py
    ├── validator.py
    ├── categorizer.py
    ├── aggregator.py
    ├── normalizer.py
    ├── duplicates.py
    ├── validator.py
    ├── statistics.py
    ├── filtering.py
    └── reporter.py
```

---

## 🧠 Technologies Used

- Python 3
- `csv` module
- `pathlib`
- `json`
- `logging`
- `argparse`
- `collections`
- `rich` (optional)

---

## ⚙️ Installation

**Clone Repository**

```bash
git clone https://github.com/BhaumikLuhar/mini-python-projects.git
cd Expense_Consolidator
```

**Create Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install Dependencies**

```bash
pip install rich
```

---

## 🚀 Usage

**Basic Run**

```bash
python3 consolidate.py expenses/
```

**Filter By Month**

```bash
python3 consolidate.py expenses/ --month 2026-01
```

**Help Menu**

```bash
python3 consolidate.py --help
```

---

## 💻 Example Terminal Output

```
TOTAL SPEND
========================================
7350.0

TOP CATEGORIES
========================================
Travel          2300.0
Infrastructure  2100.0
Meals           1950.0
Shopping        1000.0
```

---

## 📄 Input CSV Example

```
Date,AMT,Vendor,Category
2026-01-01,500,Uber,
2026-01-02,700,Swiggy,Meals
```

## 📄 Output Consolidated CSV

```
date,amount,vendor,category
2026-01-01,500,Uber,Travel
2026-01-02,700,Swiggy,Meals
```

---

## 🔑 Key Engineering Concepts Used

### Pathlib

Used for:

- File handling
- Folder traversal
- CSV discovery

### Data Validation

Prevents malformed rows from entering the pipeline.

### ETL Pipeline Design

The project follows a real-world ETL architecture:

```
LOAD CSVs
→ NORMALIZE COLUMNS
→ VALIDATE DATA
→ CATEGORIZE VENDORS
→ AGGREGATE TOTALS
→ EXPORT REPORTS
```

### Modular Architecture

Business logic is separated into reusable utility modules.

### Configuration-Driven Rules

Categorization rules are externalized in JSON for flexibility.

---

## 📈 Business Impact

### Time Savings

Manual expense consolidation typically requires:

- Cleaning spreadsheets
- Fixing inconsistent columns
- Categorizing vendors
- Calculating totals

| Method    | Estimated Effort       |
|-----------|------------------------|
| Manual    | ~20–30 minutes/dataset |
| Automated | < 5 seconds            |

### Error Reduction

The tool:

- Prevents missing-category issues
- Reduces spreadsheet mistakes
- Catches malformed rows
- Standardizes reporting

### Scalability

Supports:

- Multiple teams
- Multiple CSV formats
- Configurable categorization rules

...without modifying business logic.

---

## 🔥 Stretch Goals Implemented

- Duplicate detection
- Logging system
- Month-based filtering
- Analytics dashboard
- Rich terminal formatting

---

## 📈 Future Improvements

Potential enhancements:

- SQLite database support
- Web dashboard
- PDF reports
- Email notifications
- Machine-learning categorization
- REST API integration
- Real-time expense ingestion

---

## 🎓 Learning Outcomes

This project demonstrates understanding of:

- Functions & modular programming
- CSV processing & file handling
- `pathlib` & `json`
- Dictionaries & list comprehensions
- Data validation & aggregation pipelines
- CLI application development
- Logging & error handling

---

## 👨‍💻 Author

Built as part of a Python learning capstone project focused on:

- Data processing
- Backend fundamentals
- ETL pipeline design
- Professional software structure