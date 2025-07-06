# email_bot/email_reader.py

import imaplib
import email
import os
from email.header import decode_header
from classifier import classify_email
from decoder import process_attachments
from database import save_email_record
from loguru import logger

EMAIL_HOST = os.getenv("EMAIL_HOST", "imap.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 993))
EMAIL_USER = os.getenv("EMAIL_USER", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")

def check_inbox_and_process_emails():
    logger.info("Checking inbox...")

    with imaplib.IMAP4_SSL(EMAIL_HOST, EMAIL_PORT) as mail:
        mail.login(EMAIL_USER, EMAIL_PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, 'UNSEEN')
        # status, messages = mail.search(None, 'ALL') # Uncomment if you want to process all emails, not just unread ones
        if status != 'OK':
            logger.error("Failed to search emails.")
            return

        list_emails = messages[0].split()

        while list_emails:
            latest_email_id = list_emails[-1] # Get the most recent email ID
            status, data = mail.fetch(latest_email_id, "(RFC822)")
            if status != 'OK':
                logger.warning(f"Could not fetch message {latest_email_id}")
                continue

            msg = email.message_from_bytes(data[0][1])
            email_data = parse_email(msg)

            qr_data, boleto_data = process_attachments(msg)
            classification, keyword = classify_email(email_data, qr_data, boleto_data)

            if qr_data or boleto_data or keyword:
                mail.store(latest_email_id, '-FLAGS', '\\Seen') # Mark as unread
                save_email_record(email_data, classification, keyword, qr_data, boleto_data)
            else:
                mail.store(latest_email_id, '-FLAGS', '\\Seen') # Mark as unread

            list_emails.pop()
            # break

def parse_email(msg):
    subject = decode_mime_words(msg.get("Subject", ""))
    sender = msg.get("From", "")
    date = msg.get("Date", "")
    body = extract_body_from_email(msg)

    return {
        "subject": subject,
        "sender": sender,
        "date": date,
        "body": body
    }

def decode_mime_words(s):
    decoded, charset = decode_header(s)[0]
    if isinstance(decoded, bytes):
        return decoded.decode(charset or "utf-8", errors="replace")
    return decoded

def extract_body_from_email(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_dispo = str(part.get("Content-Disposition"))

            if content_type == "text/plain" and "attachment" not in content_dispo:
                return part.get_payload(decode=True).decode("utf-8", errors="ignore")
    else:
        return msg.get_payload(decode=True).decode("utf-8", errors="ignore")
    return ""
