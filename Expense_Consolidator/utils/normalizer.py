COLUMN_ALIASES = {
    "amt": "amount"
}


def normalize_columns(row):
    """Normalizes column names."""

    normalized={}

    for key,val in row.items():
        clean_key=key.strip().lower()
        clean_key=COLUMN_ALIASES.get(clean_key,clean_key)
        normalized[clean_key]=val

    return normalized