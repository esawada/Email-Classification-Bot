# email_bot/database.py

import mysql.connector
from mysql.connector import Error
from loguru import logger
import json
import os

# Read DB credentials from environment or fallback values
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "email_classifier")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
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
            user=DB_USER,
            password=DB_PASS
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
                content TEXT,
                classification VARCHAR(50),
                keyword VARCHAR(100),
                qr_data JSON,
                received_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)
        conn.commit()
        logger.info("Table `classified_emails` checked/created.")
        cursor.close()
        conn.close()
    except Error as e:
        logger.error(f"MySQL setup error: {e}")
        
def save_email_record(subject, sender, content, classification, keyword, qr_data):
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    
    # Convert QR data (list of dicts) to JSON string for storage
    qr_data_json = json.dumps(qr_data, ensure_ascii=False)

    query = """
        INSERT INTO classified_emails (
            subject, sender, content, classification, keyword, qr_data
        ) VALUES (%s, %s, %s, %s, %s, %s);
    """
    cursor.execute(query, (subject, sender, content, classification, keyword, qr_data_json))
    conn.commit()
    cursor.close()
    conn.close()
