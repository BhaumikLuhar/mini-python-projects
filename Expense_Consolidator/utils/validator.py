def is_blank_row(row):
    """Checks whether row is blank. Return True or False"""
    return all(value.strip()=="" for value in row.values())

def is_valid_row(row):
    """Checks required fields."""

    required = ["date", "amount", "vendor"]

    return all(field in row and row[field] for field in required)