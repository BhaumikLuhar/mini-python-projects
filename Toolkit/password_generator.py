import random,string

def passwordGen(args):
    if(args.length < 4):
        print("Password length must be at least 4.")
        return
    
    availableChar=string.ascii_lowercase

    if not args.no_numbers:
        availableChar+=string.digits

    if args.symbols:
        characters += "!@#$%^&*()_+-="

    password="".join(random.SystemRandom().choices(availableChar,k=args.length))

    print("\nSECURE PASSWORD")
    print("-" * 35)

    print(password)