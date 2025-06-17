# Email-Classification-Bot
Email Intelligence Bot (Python, Cloud, SQL) – Designed and deployed a cloud-based automation tool that continuously scans and classifies incoming emails into predefined categories (e.g., bills, QR codes, keyword alerts), stores structured data in a SQL database, and supports PDF/QR parsing. The project showcases full-stack backend development, email automation, and integration with cloud services like AWS/GCP. Ideal for showcasing real-world automation, database design, and applied NLP.

 --------------------------------------------------------------------------------------------------------

# Advanced Features I Learned during this project

- Cloud Deployment: Understanding how to deploy your bot on AWS Lambda or GCP Cloud Functions for 24/7 uptime.

- OAuth2 Authentication: For secure access to Gmail or other providers using modern security practices.

- Regex + NLP: To extract structured info from unstructured text (e.g., detect due dates, invoice numbers, payment URLs).

- QR Code Decoding: Handle embedded QR codes in attachments (PDF, PNG, etc.) and extract data from them.

- Attachment Handling: Auto-download and analyze PDF or image attachments.

- Database Indexing & Schema Design: Efficiently store classifications and retrieval logic.

- Security: Properly encrypt and store access tokens, sanitize inputs, and manage credentials.

- Email Filtering Logic: Build customizable filters (e.g., by sender, subject, or message content).

  --------------------------------------------------------------------------------------------------------

# Tech Stack

Backend

  - Language: Python

  - Email Handling: IMAP via imaplib, mailbox, or IMAPClient

  - Email Parsing: email, BeautifulSoup, pdfminer.six, PyMuPDF (to parse attachments like PDFs)

  - QR Code Detection: pyzbar, opencv-python, or zxing

  - Keyword Detection: Custom NLP logic, possibly enhanced by spaCy or scikit-learn for smarter classification

  - Scheduler / Automation: Celery with Redis (or just a cron job for simpler scheduling)

  - Database: PostgreSQL or MySQL (SQLite can be used for local testing)

  - ORM: SQLAlchemy or Django ORM

Cloud & Hosting

  - Cloud Hosting: AWS Lambda + RDS (PostgreSQL) or Google Cloud Functions + Cloud SQL

  - Email Provider Integration: Gmail API (OAuth2) or direct IMAP access (for any email provider)

  - Scheduler (Cloud): AWS EventBridge or Google Cloud Scheduler

  - Storage (Optional): S3 or Google Cloud Storage (for attachments)

Monitoring & Logging

  - Logging: loguru or structlog (Python), connected to a cloud logging service
    
  - Monitoring/Alerts: Use tools like Sentry or Grafana + Prometheus if needed
    
 --------------------------------------------------------------------------------------------------------

 # Project Roadmap

 This project was made as a personal projects to help me manage my emails. The whole project was made in 6 sprints, each a week long.

 📅 WEEK 1: Project Setup & Email Access
🎯 Goal: Set up project structure and read emails from your inbox.
Tasks:
1. Project Initialization (3h)
Set up a GitHub repo, virtual environment, and directory structure.

Tool: Python, pipenv or venv

2. Configure Email Access via IMAP (3h)
Use IMAPClient or imaplib to access inbox.

Authenticate using app password or OAuth2 (start with basic auth for testing).

Tech: imaplib, email, keyring

3. Fetch and Parse Basic Emails (3h)
Connect to mailbox and retrieve subject, sender, date, and body of recent emails.

Tech: email.message, email.utils, BeautifulSoup

4. Store Raw Email Metadata in Database (3h)
Set up PostgreSQL or SQLite locally.

Tech: PostgreSQL, SQLAlchemy

Store: subject, from, to, date, body, uid

📅 WEEK 2: Classification Engine (Part 1)
🎯 Goal: Implement basic keyword and metadata-based classification.
Tasks:
1. Setup Keyword Classification Module (3h)
Create a dictionary of keyword categories (e.g., bills, subscriptions, alerts).

Use string matching and re for regex-based keyword scans.

2. Implement Rule-Based Classifier Function (3h)
Assign categories based on:

Subject

Sender address

Body keywords

Tech: Python logic + re, json, logging

3. Store Classification Results in Database (3h)
Add category column to DB schema.

Log confidence and triggered keyword.

Tech: SQLAlchemy

4. Test Classifier on 10 Sample Emails (3h)
Build unit tests and mock emails.

Tech: pytest, unittest.mock

📅 WEEK 3: QR Code and Attachment Handling
🎯 Goal: Detect and decode QR codes from email images and PDF attachments.
Tasks:
1. Download Attachments from Emails (3h)
Parse emails with .get_payload() and save attachments.

Tech: email.message, os, tempfile

2. Detect & Decode QR Codes from Images (3h)
Use opencv or pyzbar to scan images for QR codes.

Output decoded text or URLs.

3. Extract QR Codes from PDFs (3h)
Convert PDF pages to images using PyMuPDF or pdf2image, then scan.

Tech: PyMuPDF, PIL, pyzbar

4. Classify Emails Containing QR Codes (3h)
Tag email as “QR Detected” and extract code contents.

Update DB table with qr_data field.

📅 WEEK 4: Automation & Cloud Deployment
🎯 Goal: Automate the bot and deploy it to the cloud.
Tasks:
1. Write a Scheduled Script (3h)
Use schedule or APScheduler to check emails every X minutes.

Tech: schedule, threading, time

2. Prepare for Serverless Deployment (3h)
Wrap logic into a function ready for AWS Lambda/GCP.

Move credentials/config to .env and use dotenv.

3. Set Up AWS Lambda or Google Cloud Function (6h)
Package Python code (ZIP or Docker).

Deploy and trigger using EventBridge (AWS) or Cloud Scheduler (GCP).

Tech: boto3 or GCP SDK

📅 WEEK 5: Advanced Filtering & UI Dashboard (Optional)
🎯 Goal: Add filtering rules and optional web interface.
Tasks:
1. Advanced Filters (3h)
Detect invoice numbers, due dates, totals using regex/NLP.

Tech: re, spaCy

2. Optional: Flask Admin Dashboard (6h)
Display classified emails in a simple Flask app.

Tech: Flask, Flask-SQLAlchemy, Bootstrap

📅 WEEK 6: Testing, Logging & Polish
🎯 Goal: Make the project robust and production-ready.
Tasks:
1. Add Logging (3h)
Use loguru to record pipeline steps and errors.

2. Unit + Integration Tests (3h)
Mock email inputs, attachments, classification pipeline.

3. Deployment Monitoring (3h)
Set up notifications via email or Slack for critical failures.

4. Final Documentation & README (3h)
Include tech stack, usage, architecture diagram, limitations.
