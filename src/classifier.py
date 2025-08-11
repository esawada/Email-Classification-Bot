# email_bot/classifier.py

import re
from config import KEYWORDS

keywords = KEYWORDS

def classify_email(email_data, qr_data=None, boleto_data=None):
    text = (email_data["subject"] + " " + email_data["body"]).lower()
    if boleto_data: 
        return "boleto"
    if qr_data:
        return "qr_code"

    for keyword in keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            return keyword
    return None
