from pathlib import Path


def export_html(notes, output="index.html"):
    """
    Export notes as HTML index.
    """

    html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Notes Export</title>

    <style>
        body {
            font-family: Arial;
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }

        .note {
            border-bottom: 1px solid #ccc;
            margin-bottom: 20px;
            padding-bottom: 20px;
        }

        .tags {
            color: #666;
        }
    </style>
</head>
<body>

<h1>Notes Export</h1>
"""

    for note in notes:
        html += f"""
<div class="note">
    <h2>{note['title']}</h2>

    <p class="tags">
        Tags: {", ".join(note['tags'])}
    </p>

    <p>
        {note['body'][:200]}
    </p>

    <small>{note['created']}</small>
</div>
"""

    html += """
</body>
</html>
"""

    output_path=Path(output)

    output_path.write_text(html,encoding="utf-8")

    return output_path