def detect_duplicate(expenses):
    """Detects duplicate expense rows."""

    seen=set()

    duplicates=[]

    for expense in expenses:
        identifier=(
            expense["date"],
            (expense["vendor"] or "").lower(),
            expense["amount"]
        )

        if identifier in seen:
            duplicates.append(expense)
        else:
            seen.add(identifier)
    
    return duplicates