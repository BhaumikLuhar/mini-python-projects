def convert(args):
    # if len(args) != 3:
    #     print("Usage: python toolkit.py convert <amount> <from> <to>")
    #     return

    try:
        amount = float(args.amount)
    except ValueError:
        print("Invalid amount.")
        return
    
    fromUnit=args.from_currency
    toUnit=args.to_currency

    rates = {
        ("USD", "INR"): 97.0,
        ("INR", "USD"): 1 / 97.0,
        ("EUR", "INR"): 112.0,
        ("INR", "EUR"): 1 / 112.0
    }

    key= (fromUnit, toUnit)

    if key not in rates:
        print("Unsupported conversion.")
        return
    
    converted=amount*rates[key]

    print("\nCurrency Conversion")
    print("-" * 35)

    print(f"From   : {fromUnit}")
    print(f"To     : {toUnit}")
    print(f"Amount : {amount:,.2f}")
    print(f"Result : {converted:,.2f}")