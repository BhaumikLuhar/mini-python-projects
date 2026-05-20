def slugifyText(args):
    # if len(args) != 1:
    #     print('Usage: python toolkit.py slugify "text"')
    #     return
    
    text=args.text

    text=text.strip().lower().replace(" ","-")

    print(text)