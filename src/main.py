from config import EMAIL_USER, LOG_LEVEL
from email_reader import check_inbox_and_process_emails
from database import initialize_database
from loguru import logger
import schedule
import os
import time

def main():
    CHECK_INTERVAL_MINUTES = os.getenv("CHECK_INTERVAL_MINUTES", 5)

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOG_LEVEL)

    logger.info(f"Starting Email Bot for {EMAIL_USER}")
    initialize_database()

    # Schedule the job
    check_inbox_and_process_emails()  # Initial run
    schedule.every(int(CHECK_INTERVAL_MINUTES)).minutes.do(check_inbox_and_process_emails)

    logger.info("Scheduler started. Waiting for jobs...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
