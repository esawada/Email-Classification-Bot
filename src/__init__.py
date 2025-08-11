# email_bot/__init__.py

"""
Email Classification Bot

This package handles:
- Reading emails from an IMAP server
- Classifying them by keywords
- Detecting QR codes in attachments
- Storing results in a SQL database
"""

__version__ = "0.1.0"
__author__ = "esawada"

from . import classifier
from . import database
from . import decoder
from . import email_reader

from .classifier import classify_email
from .database import get_db_connection, initialize_database, save_email_record
from .decoder import process_attachments, decode_from_image, decode_from_pdf
from .email_reader import check_inbox_and_process_emails

# Define what gets imported with `from email_reader import *`
__all__ = [
    "classify_email",
    "get_db_connection",
    "initialize_database",
    "save_email_record",
    "process_attachments",
    "decode_from_image",
    "decode_from_pdf",
    "check_inbox_and_process_emails",
]