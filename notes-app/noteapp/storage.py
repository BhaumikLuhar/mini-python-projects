from pathlib import Path
from datetime import datetime
import re

NOTES_DIR=Path("notes")
NOTES_DIR.mkdir(exist_ok=True)



def slugify(text):
    """
    Convert text into URL/file-safe slug.

    Example:
    'Meeting Notes' -> 'meeting-notes'
    """

    text=text.lower()
    text=re.sub(r"[^a-z0-9\s-]","",text)
    text=re.sub(r"\s+","-",text)
    text=re.sub(r"-+","-",text)

    return text.strip("-")


def build_note_filename(title):
    """
    Generate note filename using today's date and slug.

    Example:
    2026-05-27-meeting-notes.md
    """
    
    today=datetime.now().strftime("%Y-%m-%d")
    slug=slugify(title)

    return f"{today}-{slug}.md"


def build_note_path(title):
     """
    Build full path for a note.
    """
     
     filename=build_note_filename(title)

     return NOTES_DIR / filename


def create_note_content(title, tags=None):
    """
    Generate markdown note template with frontmatter.
    """

    if tags is None:
        tags=[]

    created=datetime.now().isoformat()
    tag_string=", ".join(tags)

    return f"""---
title: {title}
tags: {tag_string}
created: {created}
---

Write your note here...
"""


if __name__ == "__main__":

    print(slugify("Meeting with Acme!"))

    print(build_note_filename("Quarterly Planning"))

    print(build_note_path("Demo Note"))

    print(create_note_content(
        "Project Ideas",
        ["python", "cli"]
    ))