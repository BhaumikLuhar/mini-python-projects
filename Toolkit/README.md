# 🛠️ Toolkit CLI

A multi-purpose command-line productivity toolkit built with Python and argparse.

Designed to automate repetitive day-to-day utility tasks such as GST calculation, currency conversion, employee ID generation, file renaming, and text formatting.

---

# 📌 Business Value

Small repetitive tasks consume significant time across teams.

Toolkit CLI reduces manual effort by turning common operations into one-line commands.

Estimated impact:

- Saves ~3–5 minutes per task
- At 10 uses/day → ~50 minutes saved daily
- Across a team of 5 → ~80+ hours recovered monthly

The goal is operational efficiency through lightweight automation.

---

# 🚀 Features

## 1. GST Calculator

Calculates GST breakdown with:
- Base amount
- CGST
- SGST
- Final total

Supports:
- essentials (5%)
- standard (12%)
- luxury (18%)
- sin goods (28%)

### Example

```bash
python toolkit.py gst 5000 luxury
```
---

## 2. Currency Converter
 
Converts currencies using a lightweight internal FX table.
 
**Supported conversions:**
 
- USD ↔ INR
- EUR ↔ INR
**Example**
 
```bash
python toolkit.py convert 100 USD INR
```
 
---
 
## 3. Age Calculator
 
Calculates age in:
 
- Years
- Months
- Days
**Example**
 
```bash
python toolkit.py age 1990-05-15
```
 
---
 
## 4. Employee ID Generator
 
Generates random employee IDs in format:
 
```
EMP-A4G7
```
 
**Useful for:**
 
- Testing
- Demos
- Onboarding simulations
- Internal tooling
**Example**
 
```bash
python toolkit.py ids 10
```
 
---
 
## 5. File Rename Utility
 
Quickly renames files using Python automation.
 
**Example**
 
```bash
python toolkit.py rename tmp.txt monthly_report.txt
```
 
---
 
## 6. Slugify Utility
 
Converts text into URL-friendly slugs.
 
**Example**
 
```bash
python toolkit.py slugify "Hello World"
```
 
**Output**
 
```
hello-world
```
 
---

## 7. Batch File Rename
 
Bulk renames files automatically.
 
**Useful for:**
 
- Reports
- Exports
- Invoices
- Media files
- Operational documents
**Features**
 
- Preview mode
- Overwrite protection
- Folder-safe renaming
- Rename summary
**Preview Changes**
 
```bash
python toolkit.py batchrename report invoice --preview
```
 
**Execute Rename**
 
```bash
python toolkit.py batchrename report invoice
```
 
---
 
## 8. Password Generator
 
Generates secure random passwords.
 
**Features**
 
- Configurable length
- Optional symbols
- Optional numbers
- Strong randomness
**Example**
 
```bash
python toolkit.py password 16 --symbols
```
 
**Example Output**
 
```
🔐 SECURE PASSWORD
-----------------------------------
A9#xQ1@Lm2!Rt7Z
```
 
---
 
## 9. QR Code Generator
 
Generates QR codes for:
 
- URLs
- Documents
- Payment links
- Internal systems
**Example**
 
```bash
python toolkit.py qr "https://google.com" --output google_qr
```
 
**Output**
 
```
exports/google_qr.png
```
 
---
 
## 10. Command History Logging
 
Automatically logs executed commands with timestamps.
 
**Useful for:**
 
- Auditing
- Debugging
- Workflow tracking
- Operational monitoring
**Example Log Entry**
 
```
[2026-05-20 14:32:11] toolkit.py gst 5000 luxury
```
 
Logs are stored in:
 
```
toolkit.log
```
 
---
 
## 🧠 Technical Highlights
 
**Built using:**
 
- Python 3
- `argparse`
- `os`
- `datetime`
- `random`
- `string`

**Architecture principles:**
 
- Modular functions
- Command-based CLI design
- Defensive input handling
- Scalable subcommand structure
---
 
## 📂 Project Structure
 
```
Toolkit/
│
├── __pycache__/
├── age_calc.py
├── batch_rename.py
├── currency_convert.py
├── GST.py
├── id_generator.py
├── log_command.py
├── password_generator.py
├── qr_generator.py
├── rename_file.py
├── slugify.py
├── toolkit.py
├── toolkit.log
├── tmp.txt
└── README.md
```
 
---
 
## ⚙️ Installation
 
Clone the repository:
 
```bash
git clone <your-repo-url>
```
 
Move into project folder:
 
```bash
cd Toolkit
```
 
Run commands:
 
```bash
python3 toolkit.py --help
```
 
---
 
## 📖 Command Help
 
Show all commands:
 
```bash
python toolkit.py --help
```
 
Show help for one command:
 
```bash
python toolkit.py gst --help
```
 
---
 
## ✅ Error Handling
 
Toolkit CLI safely handles:
 
- Missing arguments
- Invalid input
- Unsupported conversions
- Missing files
- Invalid dates
...without crashing.
 
---
 
## 🔥 Stretch Features Implemented
 
- `argparse`-based CLI architecture
- Professional help menus
- Aligned output formatting
- Reusable modular functions
- Slug generation utility
---
 
 
## 👨‍💻 Why This Project Matters
 
This project demonstrates practical software engineering concepts:
 
- Command-line interface design
- Automation scripting
- Modular programming
- Input validation
- File handling
- Scalable architecture

The toolkit simulates real-world internal automation tools commonly used in operations, finance, and engineering teams.
 