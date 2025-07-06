# email_bot/classifier.py

import re

# Keywords organized by category
KEYWORDS = {
    "bills": ["invoice", "payment due", "bill", "due date", "total amount"],
    "alerts": ["alert", "warning", "notice", "failed"],
    "subscriptions": ["subscription", "renewal", "auto-renew"]
}

def classify_email(email_data):
    text = (email_data["subject"] + " " + email_data["body"]).lower()

    for category, keywords in KEYWORDS.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text):
                return category, keyword
    return "uncategorized", None
