# Notes App

A fast, local-first command-line notes system built with Python. Store, search, tag, and manage markdown notes with structured metadata — no cloud services, no heavy applications required.

---

## 🧩 Problem

Managing lightweight notes across meetings, ideas, and tasks often requires heavy applications or cloud services. This project provides a fast, local-first command-line notes system using markdown files with searchable metadata.

---

## ✅ Solution

Notes App is a Python CLI tool that stores notes as markdown files with structured frontmatter metadata.

The application supports:

- Note creation
- Full-text search
- Tag management
- Recent note filtering
- Safe deletion

---

## 🔥 Features

- Create markdown notes
- Automatic slug generation
- Structured frontmatter metadata
- Tag-based filtering
- Full-text search
- Recent notes filtering
- Safe deletion confirmation
- Modular architecture
- Error handling for malformed notes

---

## 🧠 Tech Stack

- Python 3
- `argparse`
- `pathlib`
- `datetime`
- `re` (regex)

---

## 📂 Project Structure

```
notes-app/
│
├── noteapp/
│   ├── storage.py
│   ├── search.py
│   ├── cli.py
│   └── main.py
│
├── notes/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

**Clone repository:**

```bash
git clone https://github.com/BhaumikLuhar/mini-python-projects.git
cd notes-app
```

**Create virtual environment:**

```bash
python -m venv .venv
```

**Activate virtual environment:**

- Windows:

```bash
.venv\Scripts\activate
```

- macOS/Linux:

```bash
source .venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

**Create note:**

```bash
python -m noteapp.main new "Quarterly Planning"
```

**List notes:**

```bash
python -m noteapp.main list
```

**Filter by tag:**

```bash
python -m noteapp.main list --tag planning
```

**Search notes:**

```bash
python -m noteapp.main search budget
```

**Show recent notes:**

```bash
python -m noteapp.main list --recent
```

**Delete note:**

```bash
python -m noteapp.main delete 2026-05-27-quarterly-planning
```

---

## 📄 Note Format

Each note is stored as a markdown file with structured frontmatter:

```markdown
---
title: Quarterly Planning
slug: 2026-05-27-quarterly-planning
date: 2026-05-27
tags: [planning, meetings]
---

Note content goes here...
```

---

## ✅ Error Handling

The application safely handles:

- Missing files
- Malformed frontmatter
- Invalid note slugs
- Duplicate note creation
- Invalid metadata

...without crashing the application.

---

## 🔑 Key Engineering Concepts Used

### Modular Architecture

Business logic is cleanly separated across focused modules:

| Module       | Responsibility                        |
|--------------|---------------------------------------|
| `storage.py` | File I/O, note saving and loading     |
| `search.py`  | Full-text and tag-based search logic  |
| `cli.py`     | Argument parsing and command routing  |
| `main.py`    | Entry point and application bootstrap |

### Slug Generation

Note filenames are auto-generated from the title and date, ensuring:

- No duplicate filenames
- Human-readable file names
- Easy retrieval by slug

### Local-First Design

All notes are stored as plain markdown files — no database, no cloud dependency, fully portable.

---

## 📈 Future Improvements

Potential enhancements:

- HTML export
- Fuzzy search
- Synced cloud folder support
- Rich terminal formatting
- Interactive note editing
- Note templates
- Archive and restore functionality

---

## 🎓 Learning Outcomes

This project demonstrates understanding of:

- CLI application design with `argparse`
- File system operations with `pathlib`
- Markdown and frontmatter parsing
- Modular Python architecture
- Data validation and error handling
- Slug generation and metadata management

---

## 👨‍💻 Author

Built as part of a Python learning project focused on:

- Local-first application design
- Backend CLI development
- Modular programming
- Professional software structure