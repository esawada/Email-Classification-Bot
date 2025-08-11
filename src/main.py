from loguru import logger
from config import EMAIL_USERNAME, CHECK_INTERVAL_MINUTES
from email_reader import check_inbox_and_process_emails
from database import initialize_database
import schedule
import os
import time

def main():

    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level="INFO")

    logger.info(f"Starting Email Bot for {EMAIL_USERNAME}...")
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
