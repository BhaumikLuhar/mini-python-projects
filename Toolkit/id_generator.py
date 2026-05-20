import string
import random

def idGenerator(args):
    # if len(args) != 1:
    #     print("Usage: python toolkit.py ids <count>")
    #     return

    try:
        count = int(args.count)
    except ValueError:
        print("Count must be a number.")
        return

    availableChar=string.ascii_uppercase+string.digits

    print("\n EMPLOYEE IDS")
    print("-" * 35)

    for _ in range(count):
        randomPart= "".join(random.choices(availableChar,k=4))
        print(f"EMP-{randomPart}")