# email_bot/database.py

import mysql.connector
from config import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD
from mysql.connector import Error
from loguru import logger
from email.utils import parsedate_to_datetime
import json
import os

# Read DB credentials from environment or fallback values

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        return connection
    except Error as e:
        logger.error(f"MySQL connection error: {e}")
        return None

def initialize_database():
    try:
        # Connect to MySQL server without selecting a DB yet
        server_conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USERNAME,
            password=DB_PASSWORD
        )
        server_cursor = server_conn.cursor()

        # 1. Create the database if it doesn't exist
        server_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        logger.info(f"Database `{DB_NAME}` checked/created.")

        server_cursor.close()
        server_conn.close()

        # 2. Connect to the specific database to create the table
        conn = get_db_connection()
        if not conn:
            return

        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classified_emails (
                id INT AUTO_INCREMENT PRIMARY KEY,
                subject VARCHAR(255),
                sender VARCHAR(255),
                date DATETIME,
                body TEXT,
                keyword VARCHAR(100),
                qr_data JSON,
                boleto_data JSON
            );
        """)
        conn.commit()
        logger.info("Table `classified_emails` checked/created.")
        cursor.close()
        conn.close()
    except Error as e:
        logger.error(f"MySQL setup error: {e}")
        
def save_email_record(email_data, keyword, qr_data = None, boleto_data = None):
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    
    # Convert QR data (list of dicts) to JSON string for storage
    qr_data_json = json.dumps(qr_data, ensure_ascii=False)
    boleto_data_json = json.dumps(boleto_data, ensure_ascii=False)

    # Parse the date string to a datetime object
    dt = parsedate_to_datetime(email_data["date"])
    mysql_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")

    query = """
        INSERT INTO classified_emails (
            subject, sender, date, body, keyword, qr_data, boleto_data
        ) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, (email_data["subject"], email_data["sender"], mysql_datetime, email_data["body"], keyword, qr_data_json, boleto_data_json))
    conn.commit()
    cursor.close()
    conn.close()
    logger.info(f"Email saved: {email_data['subject']} with the keyword {keyword}.")

