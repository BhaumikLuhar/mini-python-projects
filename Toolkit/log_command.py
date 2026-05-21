from datetime import datetime

def logCommand(argv):
    command=" ".join(argv)

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(
        "toolkit.log",
        "a",
        encoding="utf-8"
    ) as file:
        file.write(
            f"[{timestamp}] : {command}\n"
        )