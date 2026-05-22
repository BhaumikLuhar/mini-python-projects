import csv
from pathlib import Path

from utils.normalizer import normalize_columns
from utils.validator import (
    is_blank_row,
    is_valid_row
)
import logging

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="warnings.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"    
)

def load_csvs(folder):
    """Loads all CSVs from folder."""

    expenses=[]

    csv_files=Path(folder).glob("*.csv")

    for file in csv_files:

        with open(file,"r") as f:
            reader=csv.DictReader(f)

            for row in reader:
                row=normalize_columns(row)
                # print(row)
                if is_blank_row(row):
                    continue

                if not is_valid_row(row):
                    logging.warning(
                        f"Bad row in {file.name}: {row}"
                    )

                    continue

                expenses.append(row)

    return expenses