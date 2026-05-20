def calculateGST(args):
    # if len(args) != 2:
    #     print("Usage: python toolkit.py gst <amount> <category>")
    #     return
    
    try:
        amount=float(args.amount)
    except ValueError:
        ("Invalid amount.")
        return
    
    category=args.category.strip().lower()
    gstRate={
        "essentials": 5,
        "standard": 12,
        "luxury": 18,
        "sin": 28
    }

    if category not in gstRate:
        print("Unknown category.")
        return
    
    gst_rate=gstRate[category]

    gstAmt=amount*gst_rate/100
    cgst=gstAmt/2
    sgst=gstAmt/2
    totAmt=amount+gstAmt

    print("\nGST BILL")
    print("-" * 35)

    print(f"{'Category':<15} : {category.title():>10}")
    print(f"{'Base Amount':<15} : {amount:>10.2f}")
    print(f"{'CGST':<15} : {cgst:>10.2f}")
    print(f"{'SGST':<15}: ₹{sgst:>10,.2f}")

    print("-" * 35)

    print(f"{'TOTAL':<15}: ₹{totAmt:>10,.2f}")