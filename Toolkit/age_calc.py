from datetime import datetime

def ageCalc(args):
    # if len(args) != 1:
    #     print("Usage: python toolkit.py age <YYYY-MM-DD>")
    #     return
    
    try:
        birth_date = datetime.strptime(args.birthdate, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return
    
    today=datetime.today()
    days=(today-birth_date).days
    
    years=days // 365
    months=(days%365) // 30
    remainingDays=(days%365)%30

    print("\nAGE REPORT")
    print("-" * 35)

    print(f"Years  : {years}")
    print(f"Months : {months}")
    print(f"Days   : {remainingDays}")
