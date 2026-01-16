import pandas as pd
import os
import logging
from config import GOOGLE_FORM_LINK, EMAIL_SUBJECT
from email_sender import get_gmail_service, send_email

os.makedirs("output/manager_excels", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/mail.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# df = pd.read_excel("input/employees.xlsx")  # Use this line for actual usecase
df = pd.read_excel("input/test_employees.xlsx")  


grouped = df.groupby(["Manager Name", "Manager Email"])

service = get_gmail_service()

for (manager_name, manager_email), group in grouped:
    try:
        safe_name = manager_name.replace(" ", "_")
        file_path = f"output/manager_excels/{safe_name}.xlsx"

        group.to_excel(file_path, index=False)

        email_body = f"""
Hi {manager_name},

Attached is the list of employees reporting to you.

Please fill the required details using the Google Form:
{GOOGLE_FORM_LINK}

Regards,
HR Team
"""

        send_email(
            service,
            manager_email,
            EMAIL_SUBJECT,
            email_body,
            file_path
        )

        logging.info(f"Email sent to {manager_email}")

    except Exception as e:
        logging.error(f"Failed for {manager_email}: {e}")
