from datetime import datetime, timedelta
import re

def matches_query(note, query):
    """
    Check if query exists in title, tags, or body.
    Case-insensitive.
    """

    query=query.lower()

    searchable_text=" ".join([note["title"]," ".join(note["tags"]),note["body"]]).lower()

    return query in searchable_text


def build_snippet(body,query,length=80):
    """
    Build preview snippet around search query.
    """

    body_lower=body.lower()
    query_lower=query.lower()

    index=body_lower.find(query_lower)

    if index==-1:
        return body[:length]+"..."

    start=max(index-30,0)
    end=min(index+length,len(body))

    snippet=body[start:end]

    return ("..." if start!=0 else "")+snippet.replace("\n"," ")+("..." if end!=len(body) else "")


def search_notes(notes,query):
    """
    Search notes for query matches.
    """

    results=[]

    for note in notes:
        if matches_query(note,query):
            snippet=build_snippet(note["body"],query)

            results.append({
                "title": note["title"],
                "slug": note["slug"],
                "tags": note["tags"],
                "created": note["created"],
                "snippet": snippet
            })

    return results


def filter_by_tag(notes, tag):
    """
    Return notes containing specified tag.
    """

    tag=tag.lower()
    filtered=[]

    for note in notes:
        note_tags=[t.lower() for t in note["tags"]]

        if tag in note_tags:
            filtered.append(note)

    return filtered


def filter_recent_notes(notes, days):
    """
    Return notes from last N days.
    """

    cutoff=datetime.now()-timedelta(days=days)

    filtered=[]

    for note in notes:
        try:
            created=datetime.fromisoformat(note["created"])

            if(created>=cutoff):
                filtered.append(note)
        except ValueError:
            continue

    return filtered

if __name__ == "__main__":

    sample_notes = [
        {
            "title": "Quarterly Planning",
            "tags": ["planning", "finance"],
            "body": "Discussed hiring and engineering budget.",
            "slug": "quarterly-planning",
            "created": datetime.now().isoformat()
        },
        {
            "title": "Python CLI Ideas",
            "tags": ["python"],
            "body": "Built a markdown notes application.",
            "slug": "python-cli-ideas",
            "created": datetime.now().isoformat()
        }
    ]

    print("\nSearch Results:")
    print(search_notes(sample_notes, "budget"))

    print("\nTag Filter:")
    print(filter_by_tag(sample_notes, "python"))

    print("\nRecent Notes:")
    print(filter_recent_notes(sample_notes, 30))