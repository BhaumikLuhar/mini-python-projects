def filter_by_month(expenses,month):
    """Filters expenses by month."""

    filtered=[]

    for expense in expenses:
        if expense["date"].startswith(month):
            filtered.append(expense)

    return filtered