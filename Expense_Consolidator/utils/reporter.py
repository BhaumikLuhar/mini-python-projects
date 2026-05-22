import csv


def write_consolidated(expenses, path):
    """Writes consolidated CSV."""

    fieldnames=expenses[0].keys()

    with open(path,"w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(expenses)

def write_summary(summary,path):
    """Writes category summary."""

    with open(path,"w",newline="") as f:
        writer=csv.writer(f)

        writer.writerow(["category", "Total"])

        for category, total in summary.items():
            writer.writerow([category,round(total,2)])