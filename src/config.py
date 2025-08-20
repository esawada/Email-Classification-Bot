import os, sys, json
from dotenv import load_dotenv

load_dotenv()

# Locate the config file in the same folder as the script/exe
if getattr(sys, 'frozen', False):
    # Running as compiled exe
    base_dir = os.path.dirname(sys.executable)
else:
    # Running as script
    base_dir = os.path.dirname(__file__)

config_path = os.path.join(base_dir, "config.json")

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

#config.json

# Email settings
EMAIL_HOST = config["email"]["imap_host"]
EMAIL_PORT = config["email"]["imap_port"]
EMAIL_USERNAME = config["email"]["username"]
EMAIL_PASSWORD = config["email"]["password"]

# Database settings
DB_HOST = config["database"]["db_host"]
DB_NAME = config["database"]["db_name"]
DB_USERNAME = config["database"]["username"]
DB_PASSWORD = config["database"]["password"]

# Other config
CHECK_EMAILS_SINCE_DAYS = config["other_config"]["check_emails_since_days"]
CHECK_INTERVAL_MINUTES = config["other_config"]["check_interval_minutes"]
CHECK_SEEN_EMAILS = config["other_config"]["check_seen_emails"]
MARK_EMAILS_AS_READED = config["other_config"]["mark_emails_as_readed"]

# Classification keywords
KEYWORDS = config["classification"]["keywords"]

#.env

# # Email settings
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_PORT = int(os.getenv('EMAIL_PORT', 993))
# EMAIL_USERNAME = os.getenv('EMAIL_USERNAME')
# EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# # Database settings
# DB_HOST = os.getenv('DB_HOST')
# DB_NAME = os.getenv('DB_NAME')
# DB_USERNAME = os.getenv('DB_USERNAME')
# DB_PASSWORD = os.getenv('DB_PASSWORD')

# # Other config
# CHECK_EMAILS_SINCE_DAYS = int(os.getenv('CHECK_EMAILS_SINCE_DAYS', 7))
# CHECK_INTERVAL_MINUTES = os.getenv('CHECK_INTERVAL_MINUTES', 5)
# CHECK_SEEN_EMAILS = os.getenv('CHECK_SEEN_EMAILS', 'false').lower() == 'true'
# MARK_EMAILS_AS_READED = os.getenv('MARK_EMAILS_AS_READED', 'false').lower() == 'true'

# # Classification keywords
# KEYWORDS = os.getenv('KEYWORDS', '').split(',')