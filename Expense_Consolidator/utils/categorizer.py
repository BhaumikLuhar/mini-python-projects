import json 

def loadRules(path):
    """Loads categorization rules."""
    with open(path,"r") as f:
        reader=json.load(f)

    return reader

def categorize(vendor, rules):
    """Returns category for vendor."""

    vendor=(vendor or "").strip().lower()
    for cate,van in rules.items():
        normalized=[
            (v or "").strip().lower() for v in van
        ]

        if vendor in normalized:
            return cate
    return "Other"