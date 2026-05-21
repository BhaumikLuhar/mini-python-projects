import os

def batchRename(args):
    renamed=0

    print("\nBATCH RENAME")
    print("-" * 45)

    for item in os.listdir():
        if not os.path.isfile(item):
            continue

        if(args.old not in item):
            continue

        newName= item.replace(args.old,args.new)

        if os.path.exists(newName):
            print(f"Skipped (exists): {newName}")
            continue

        if args.preview:
            print(f"[PREVIEW] {item} → {newName}")
        else:
            os.rename(item,newName)
            print(f"{item} → {newName}")

            renamed += 1
        
    if args.preview:
        print("Preview complete. No files renamed.")

    else:
        print(f"Total files renamed: {renamed}")