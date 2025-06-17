from email_bot.config import EMAIL_USER, LOG_LEVEL
from email_bot.email_reader import check_inbox_and_process_emails
from loguru import logger
import schedule
import time

def main():
    logger.remove()
    logger.add(lambda msg: print(msg, end=""), level=LOG_LEVEL)

    logger.info(f"Starting Email Bot for {EMAIL_USER}")

    # Schedule the job
    schedule.every().minutes.do(check_inbox_and_process_emails)

    logger.info("Scheduler started. Waiting for jobs...")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
