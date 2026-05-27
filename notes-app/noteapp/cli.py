import argparse
import os
from re import error
import subprocess

from noteapp.storage import (
    create_note,
    load_all_notes,
    save_note,
    delete_note
)

from noteapp.search import (
    search_notes,
    filter_by_tag,
    filter_recent_notes
)
APP_VERSION = "1.0.0"

def handle_new(args):
    """
    Create a new note.
    """
    if not args.title.strip():
        print("Error: Title cannot be empty.")
        return
    
    try:
        path=create_note(args.title)

        print(f"Created note: {path}")

        editor = os.environ.get("EDITOR")

        if editor:
            subprocess.run([editor, str(path)])


    except FileExistsError as e:
        print(f"Error: {e}")


def handle_list(args):
    """
    List notes with optional filters.
    """

    notes=load_all_notes()

    if args.tag:
        notes=filter_by_tag(notes,args.tag)
    
    if args.last:
        notes=filter_recent_notes(notes,args.last)

    if not notes:
        print("No notes found.")
        return
    
    for note in notes:
        print(f"- {note['slug']}")

        print(f"  Title: {note['title']}")

        print(f"  Tags: {', '.join(note['tags'])}")

        print(f"  Created: {note['created']}")

        print()


def handle_search(args):
    """
    Search notes.
    """

    notes=load_all_notes()

    results=search_notes(notes,args.query)

    if not results:
        print("No matches found.")
        return

    for result in results:

        print(f"- {result['slug']}")

        print(f"  Title: {result['title']}")

        print(f"  Tags: {', '.join(result['tags'])}")

        print(f"  Snippet: {result['snippet']}")

        print()


def find_note_by_slug(notes, slug):
    """
    Find note by slug.
    """

    for note in notes:

        if note["slug"] == slug:
            return note

    return None


def handle_tag(args):
    """
    Add tag to note.
    """

    notes=load_all_notes()

    note=find_note_by_slug(notes,args.slug)

    if not note:
        print("Note not found.")
        return

    if args.newtag not in note["tags"]:
        note["tags"].append(args.newtag)

    save_note(note)

    print("Tag added successfully.")


def handle_delete(args):
    """
    Delete note after confirmation.
    """

    notes = load_all_notes()

    note = find_note_by_slug(
        notes,
        args.slug
    )

    if not note:
        print("Note not found.")
        return
    
    confirm = input(
    f"Delete '{note['title']}'? Type 'yes' to confirm: "
)

    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return
    
    delete_note(note["path"])

    print("Note deleted.")



def run():
    """
    Main CLI entrypoint.
    """

    parser=argparse.ArgumentParser(description="""Markdown Notes CLI

Create, search, tag, and manage markdown notes.""")
    parser.add_argument(
    "--version",
    action="version",
    version=f"%(prog)s {APP_VERSION}"
)
    subparsers=parser.add_subparsers(dest="command")

    new_parser=subparsers.add_parser("new",help="Create new file.")
    new_parser.add_argument(
        "title",
        help="Note title"
    )

    new_parser.set_defaults(
        func=handle_new
    )

    list_parser = subparsers.add_parser(
        "list",
        help="List notes"
    )

    list_parser.add_argument(
        "--tag",
        help="Filter by tag"
    )

    list_parser.add_argument(
        "--last",
        type=int,
        help="Filter by last N days"
    )

    list_parser.set_defaults(
        func=handle_list
    )

    search_parser = subparsers.add_parser(
        "search",
        help="Search notes"
    )

    search_parser.add_argument(
        "query",
        help="Search query"
    )

    search_parser.set_defaults(
        func=handle_search
    )


    tag_parser = subparsers.add_parser(
        "tag",
        help="Add tag to note"
    )

    tag_parser.add_argument(
        "slug",
        help="Note slug"
    )

    tag_parser.add_argument(
        "newtag",
        help="Tag to add"
    )

    tag_parser.set_defaults(
        func=handle_tag
    )


    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete note"
    )

    delete_parser.add_argument(
        "slug",
        help="Note slug"
    )

    delete_parser.set_defaults(
        func=handle_delete
    )


    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    try:
        args.func(args)

    except Exception as error:
        print(f"Unexpected error: {error}")