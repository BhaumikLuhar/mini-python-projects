import os

def renameFile(args):
    # if len(args) != 2:
    #     print("Usage: python toolkit.py rename <old_file> <new_name>")
    #     return
    
    oldFile=args.old_file
    newFile=args.new_name

    if not os.path.exists(oldFile):
        print("File does not exist.")
        return
    
    extension = os.path.splitext(oldFile)[1]

    newName=newFile+extension

    os.rename(oldFile,newFile)
    print(f"Renamed '{oldFile}' → '{newFile}'")