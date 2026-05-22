from collections import defaultdict
import logging

def safe_float(value):
    """Safely converts to float."""
    return float(value or 0.0)

    
def aggregate(expenses):
    """Aggregates totals by category."""

    totals=defaultdict(float)

    for expense in expenses:
        category=expense["category"]
        amount=safe_float(expense["amount"])
        if amount is None:
            logging.warning(f"Invalid amount: {expense}")
            continue
        totals[category]+=amount

    return dict(totals)