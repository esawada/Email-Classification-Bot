# email_bot/classifier.py

import re

# Keywords organized by category
KEYWORDS = {
    "bills": ["invoice", "payment due", "bill", "due date", "total amount"],
    "alerts": ["alert", "warning", "notice", "failed"],
    "subscriptions": ["subscription", "renewal", "auto-renew"]
}

def classify_email(email_data, qr_data=None, boleto_data=None):
    text = (email_data["subject"] + " " + email_data["body"]).lower()
    if boleto_data: 
        return "boleto", None
    if qr_data:
        return "qr_code", None
    
    for category, keywords in KEYWORDS.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                return category, keyword
    return "uncategorized", None
