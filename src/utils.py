# email_bot/utils.py

import re

def clean_email_address(email_str):
    """Extract email address from a string like 'John <john@example.com>'"""
    match = re.search(r'[\w\.-]+@[\w\.-]+', email_str)
    return match.group(0) if match else email_str
