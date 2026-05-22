import sys
from pathlib import Path

from utils.loader import load_csvs
from utils.categorizer import (
    loadRules,
    categorize
)
from utils.aggregator import aggregate
from utils.reporter import (
    write_consolidated,
    write_summary
)
from utils.statistics import (
    print_stats, 
    category_stats, 
    calculate_stats, 
    print_category_stats
)
import argparse

from config import (
    CONSOLIDATED_FILE,
    SUMMARY_FILE
)
from utils.duplicates import detect_duplicate
from utils.filtering import filter_by_month
from rich.table import Table
from rich.console import Console

console = Console()



def main():
    parser=argparse.ArgumentParser(description="CSV consolidator")
    parser.add_argument("folder",help="Provide folder name")
    parser.add_argument("--month",help="Filter by month YYYY-MM")
    parser.add_argument("--stats",help="Stat matrix of data",action="store_true")
    parser.add_argument("--catstat",help="Category stat matrix",action="store_true")
    args=parser.parse_args()
    folder=args.folder

    expenses=load_csvs(folder)
    if args.month:
        expenses = filter_by_month(
            expenses,
            args.month
        )



    if args.stats:
        stat=calculate_stats(expenses)
        print_stats(stat)

    if args.catstat:
        cat_stat=category_stats(expenses)
        print_category_stats(cat_stat)

    rules=loadRules("rules.json")

    for expense in expenses:
        category=(expense.get("category") or "").strip()

        if not category:
            expense["category"]=categorize(expense["vendor"],rules)

    summary=aggregate(expenses)

    write_consolidated(expenses,CONSOLIDATED_FILE)
    write_summary(summary,SUMMARY_FILE)

    total= sum(float(amt["amount"] or 0.0) for amt in expenses)

    print("\nTOTAL SPEND")
    print("=" * 40)
    print(round(total, 2))

    print("\nTOP CATEGORIES")
    print("=" * 40)

    sorted_category=sorted(summary.items(), key = lambda x:x[1], reverse=True)

    for category, total in sorted_category[:5]:
        print(category, round(total, 2))

    duplicates = detect_duplicate(expenses)

    print("\nDUPLICATES FOUND")
    print("=" * 40)

    for duplicate in duplicates:
        print(duplicate)


if __name__ == "__main__":
    main()