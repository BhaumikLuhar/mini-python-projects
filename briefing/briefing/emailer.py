import os 
import smtplib
from email.message import EmailMessage

def send_email(subject:str, body: str,)-> None:
    sender=os.getenv("EMAIL_ADDRESS")
    password=os.getenv("EMAIL_PASSWORD")
    recipient=os.getenv("EMAIL_RECIPIENT")
    
    if not all(
        [sender, password, recipient]
    ):
        raise RuntimeError(
            "Missing email environment variables"
        )
    assert sender is not None
    assert password is not None
    assert recipient is not None
    message=EmailMessage()

    message["Subject"]=subject
    message["From"]=sender
    message["To"]=recipient

    message.set_content(body)

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
    ) as smtp:

        smtp.login(
            sender,
            password,
        )

        smtp.send_message(message)
