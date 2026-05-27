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


def create_note(title,tags=None):
    """
    Create a new markdown note file.
    """

    path=build_note_path(title)
    content=create_note_content(title,tags)

    with open(path,"w",encoding="utf-8") as f:
        f.write(content)

    return path


def parse_frontmatter(content):
    """
    Parse markdown frontmatter and body.
    """
     
    pattern = r"^---\n(.*?)\n---\n(.*)$"

    match=re.search(pattern,content,re.DOTALL)

    if not match:
        raise ValueError("Malformed frontmatter")
    
    metadata_block=match.group(1)
    body=match.group(2).strip()

    metadata={}

    for line in metadata_block.splitlines():
        if ":" not in line:
            continue

        key,value=line.split(":",1)
        metadata[key.strip()]=value.strip()

    if "tags" in metadata:
        metadata["tags"]=[
            tag.strip() for tag in metadata["tags"].split(",") if tag.strip()
        ]

    return metadata, body


def load_note(path):
    """
    Load and parse a markdown note.
    """

    try:
        with open(path,"r", encoding="utf-8")as f:
            content=f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Note not found: {path}")
    
    metadata,body=parse_frontmatter(content)

    note={
        "title":metadata.get("title",""),
        "tags":metadata.get("tags",[]),
        "created":metadata.get("created",""),
        "body": body,
        "path": str(path),
        "slug": Path(path).stem

    }

    return note

def save_note(note):
    """
    Save updated note back to disk.
    """

    tag_string=", ".join(note["tags"])

    content = f"""---
title: {note['title']}
tags: {tag_string}
created: {note['created']}
---

{note['body']}
"""
    
    with open(note["path"],"w",encoding="utf-8")as f:
        f.write(content)



def load_all_notes():
    """
    Load all markdown notes.
    """

    notes=[]

    for path in NOTES_DIR.glob("*.md"):

        try:
            note=load_note(path)
            notes.append(note)

        except ValueError as error:
            print(f"Warning: {path} skipped ({error})")

    return notes


def delete_note(path):
    """
    Delete a note file.
    """

    path=Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Note not found: {path}")

    path.unlink()








# if __name__ == "__main__":

#     created_path = create_note(
#         "Backend Architecture",
#         ["python", "storage"]
#     )

#     print("Created:", created_path)

#     note = load_note(created_path)

#     print("\nLoaded Note:")
#     print(note)

#     print("\nAll Notes:")
#     print(load_all_notes())
