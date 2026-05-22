import statistics
from rich.table import Table
from rich.console import Console

console = Console()

def calculate_stats(expenses):

    amounts = [
        float(e["amount"])
        for e in expenses
    ]

    return {
        "total": sum(amounts),
        "average": statistics.mean(amounts),
        "median": statistics.median(amounts),
        "max": max(amounts),
        "min": min(amounts),
        "count": len(amounts)
    }

from collections import defaultdict


def category_stats(expenses):
    """Returns category analytics."""

    totals = defaultdict(float)

    counts = defaultdict(int)

    for expense in expenses:

        category = expense["category"]

        amount = float(expense["amount"])

        totals[category] += amount

        counts[category] += 1

    result = {}

    for category in totals:

        result[category] = {
            "total": totals[category],
            "transactions": counts[category]
        }

    return result


def print_stats(stats):

    table = Table(title="Expense Statistics")

    table.add_column("Metric")
    table.add_column("Value")

    for key, value in stats.items():

        table.add_row(
            key,
            str(round(value, 2))
        )

    console.print(table)


def print_category_stats(category_data):

    table = Table(title="Category Analytics")

    table.add_column("Category")
    table.add_column("Total")
    table.add_column("Transactions")

    for category, data in category_data.items():

        table.add_row(
            category,
            str(round(data["total"], 2)),
            str(data["transactions"])
        )

    console.print(table)