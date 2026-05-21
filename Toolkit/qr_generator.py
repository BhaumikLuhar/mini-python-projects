import qrcode

def qrGen(args):
    try:
        img=qrcode.make(args.text)
        filename=args.output + ".png"

        img.save(filename)

        print("\nQR Code Generated")
        print("-" * 35)

        print(f"Saved as: {filename}")
    except Exception as e:
        print(f"Error: {e}")