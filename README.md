# HR Manager Automation – HR Email & Excel Workflow

This project automates a common HR workflow:

- Read a master Excel file containing employees and their managers
- Generate manager-wise Excel files
- Email each manager their respective file automatically
- Use Gmail API (OAuth) for secure email delivery

This is a production-style automation project.

---

## Features

- Groups employees by manager (scales to thousands of records)
- Generates one Excel file per manager
- Sends personalized emails with attachments
- Secure Gmail API authentication (OAuth 2.0)
- Logging for audit and debugging

---

## Tech Stack

- Python 3.9+
- pandas
- openpyxl
- Google Gmail API
- OAuth 2.0

---

## Project Structure

manager-automation/

│

├── main.py

├── email_sender.py

├── config.py

├── credentials.json   (not committed)

├── token.json         (auto-generated)

├── input/ 

│   └── employees.xlsx

├── output/

│   └── manager_excels/

├── logs/

│   └── mail.log

└── .gitignore

---

## Input Excel Format

The input Excel file must contain the following columns:

Employee Name | Employee Email | Manager Name | Manager Email

---

## Gmail API Setup (One-Time)

1. Create a Google Cloud project
2. Enable Gmail API
3. Create OAuth credentials (Desktop App)
4. Configure OAuth consent screen (External)
5. Add gmail.send scope
6. Add your Gmail as a Test User
7. Download credentials.json

---

## How to Run

### Install dependencies

pip install pandas openpyxl google-api-python-client google-auth google-auth-oauthlib

### Add input file

Place your Excel file at:
input/employees.xlsx

### First-time authentication

python auth_test.py

A browser window will open. Login and allow access.
This generates token.json.

### Run automation

python main.py

---

## Output

- Manager-wise Excel files in output/manager_excels/
- Emails sent to managers
- Logs stored in logs/mail.log

---

## Security Notes

- Do NOT commit credentials.json or token.json
- Both are included in .gitignore

---

## Use Cases

- HR data verification
- Manager reporting workflows
- Internal automation tasks

---

## Author

Built as a real-world backend automation project.
