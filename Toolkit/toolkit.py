import sys,argparse
from GST import calculateGST
from currency_convert import convert
from age_calc import ageCalc
from id_generator import idGenerator
from rename_file import renameFile
from slugify import slugifyText

def usage():

    print("""
🛠️  TOOLKIT CLI

Usage:
    python toolkit.py <command> [arguments]

Commands:

    gst <amount> <category>
        Calculate GST bill
        Categories:
            essentials = 5%
            standard   = 12%
            luxury     = 18%
            sin        = 28%

        Example:
            python toolkit.py gst 5000 luxury


    convert <amount> <from> <to>
        Currency converter

        Supported:
            USD INR
            INR USD
            EUR INR
            INR EUR

        Example:
            python toolkit.py convert 100 USD INR


    age <YYYY-MM-DD>
        Calculate exact age

        Example:
            python toolkit.py age 1990-05-15


    ids <count>
        Generate employee IDs

        Example:
            python toolkit.py ids 10


    rename <old_file> <new_name>
        Rename a file

        Example:
            python toolkit.py rename notes.txt my_notes


    slugify "<text>"
        Convert text into URL slug

        Example:
            python toolkit.py slugify "Hello World"


""")

parser=argparse.ArgumentParser(description="Took kit")

subparsers=parser.add_subparsers(dest="command")

gst_parser=subparsers.add_parser("gst", help="Calculate GST bill")
gst_parser.add_argument("amount", type= float, help="Base amount")
gst_parser.add_argument(
        "category",
        choices=[
            "essentials",
            "standard",
            "luxury",
            "sin"
        ],
        help="GST category"
    )
gst_parser.set_defaults(func=calculateGST)

convert_parser=subparsers.add_parser("convert", help="currency converter")
convert_parser.add_argument(
        "amount",
        type=float,
        help="Amount to convert"
    )
convert_parser.add_argument(
        "from_currency",
        help="Source currency"
    )
convert_parser.add_argument(
        "to_currency",
        help="Target currency"
    )
convert_parser.set_defaults(func=convert)

age_parser = subparsers.add_parser(
        "age",
        help="Calculate age"
    )
age_parser.add_argument(
        "birthdate",
        help="Birthdate YYYY-MM-DD"
    )
age_parser.set_defaults(func=ageCalc)

ids_parser = subparsers.add_parser(
        "ids",
        help="Generate employee IDs"
    )
ids_parser.add_argument(
        "count",
        type=int,
        help="Number of IDs"
    )
ids_parser.set_defaults(func=idGenerator)

rename_parser = subparsers.add_parser(
        "rename",
        help="Rename a file"
    )
rename_parser.add_argument(
        "old_file",
        help="Current filename"
    )
rename_parser.add_argument(
        "new_name",
        help="New filename"
    )
rename_parser.set_defaults(func=renameFile)

slug_parser = subparsers.add_parser(
        "slugify",
        help="Convert text into slug"
    )
slug_parser.add_argument(
        "text",
        help="Text to slugify"
    )
slug_parser.set_defaults(func=slugifyText)

args=parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()