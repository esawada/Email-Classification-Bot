import os
from dotenv import load_dotenv

load_dotenv()

# Email settings
EMAIL_HOST = os.getenv('EMAIL_HOST')            # e.g., 'imap.gmail.com'
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 993))  # IMAP SSL port
EMAIL_USER = os.getenv('EMAIL_USER')            # your email address
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')    # use app-specific password or OAuth token

# Database settings
DB_URL = os.getenv('DATABASE_URL')              # e.g., 'postgresql://user:pass@localhost/emailbot'

# Other config
CHECK_INTERVAL_MINUTES = int(os.getenv('CHECK_INTERVAL_MINUTES', 10))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
