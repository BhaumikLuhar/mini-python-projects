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
- Fuzzy search support
- Recent notes filtering
- Tag management
- Safe deletion with confirmation
- In-editor note editing via `EDITOR` variable
- HTML export
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
│   ├── export.py
│   ├── cli.py
│   └── main.py
│
├── notes/
├── exports/
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

### 1. Create a Note

Creates a new markdown note with auto-generated slug and frontmatter. Opens in your configured editor automatically if `EDITOR` is set.

```bash
python -m noteapp.main new "Quarterly Planning"
```

**Output:**

```
Created note: notes/2026-05-27-quarterly-planning.md
```

---

### 2. List Notes

Lists all notes with title, tags, and creation date.

```bash
python -m noteapp.main list
```

**Filter by tag:**

```bash
python -m noteapp.main list --tag planning
```

**Filter by last N days:**

```bash
python -m noteapp.main list --last 7
```

---

### 3. Search Notes

Performs full-text search across all note content and metadata.

```bash
python -m noteapp.main search budget
```

**Output:**

```
- 2026-05-27-quarterly-planning
  Title: Quarterly Planning
  Tags: planning, meetings
  Snippet: ...reviewed the budget for Q3...
```

---

### 4. Fuzzy Search

Finds notes even with partial or approximate matches — useful when you can't remember the exact keyword.

```bash
python -m noteapp.main search quaterly
```

Returns results even if the query doesn't exactly match note content.

---

### 5. Add Tag to Note

Adds a new tag to an existing note by slug.

```bash
python -m noteapp.main tag 2026-05-27-quarterly-planning finance
```

**Output:**

```
Tag added successfully.
```

---

### 6. Edit a Note

Opens an existing note in your configured terminal editor.

```bash
export EDITOR=code
python -m noteapp.main edit 2026-05-27-meeting-notes
```

Supported editors: `code`, `vim`, `nano`, `nvim`, or any editor available in your `PATH`.

If `EDITOR` is not set:

```
EDITOR environment variable is not set.
```

---

### 7. Delete a Note

Safely deletes a note after explicit confirmation.

```bash
python -m noteapp.main delete 2026-05-27-quarterly-planning
```

**Prompt:**

```
Delete 'Quarterly Planning'? Type 'yes' to confirm:
```

**If cancelled:**

```
Deletion cancelled.
```

---

### 8. Export Notes to HTML

Exports all notes into a single structured HTML file.

```bash
python -m noteapp.main export
```

**Output:**

```
Exported HTML to: exports/notes.html
```

Useful for sharing notes, archiving, or viewing in a browser.

---

### 9. Version Info

```bash
python -m noteapp.main --version
```

**Output:**

```
main.py 1.0.0
```

---

### 10. Help Menu

```bash
python -m noteapp.main --help
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

| Module       | Responsibility                              |
|--------------|---------------------------------------------|
| `storage.py` | File I/O, note saving and loading           |
| `search.py`  | Full-text, fuzzy, and tag-based search      |
| `export.py`  | HTML export of all notes                    |
| `cli.py`     | Argument parsing and command routing        |
| `main.py`    | Entry point and application bootstrap       |

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

- Synced cloud folder support
- Rich terminal formatting
- Note templates
- Archive and restore functionality
- SQLite-backed note indexing
- PDF export
- Batch tag operations

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