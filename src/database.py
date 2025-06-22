# email_bot/database.py

import mysql.connector
from mysql.connector import Error
from loguru import logger
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
            received_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def save_classified_email(subject, sender, content, classification, keyword):
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    query = """
        INSERT INTO classified_emails (subject, sender, content, classification, keyword)
        VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(query, (subject, sender, content, classification, keyword))
    conn.commit()
    cursor.close()
    conn.close()
# email_bot/database.py

import mysql.connector
from mysql.connector import Error
from loguru import logger
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
            received_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def save_classified_email(subject, sender, content, classification, keyword):
    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()
    query = """
        INSERT INTO classified_emails (subject, sender, content, classification, keyword)
        VALUES (%s, %s, %s, %s, %s);
    """
    cursor.execute(query, (subject, sender, content, classification, keyword))
    conn.commit()
    cursor.close()
    conn.close()
