# Email-Classification-Bot
Email Intelligence Bot (Python, SQL, IMAP) – Designed and builded as a executable. Automation tool that continuously scans and classifies incoming emails into predefined categories (e.g., bills, QR codes, keyword alerts), stores structured data in a SQL database, and supports Bar Code and QR Code scanning. The project showcases full-stack backend development, email automation, and database storage. Ideal for showcasing real-world automation, database design, and applied NLP.

 --------------------------------------------------------------------------------------------------------

 # Setup

 1. Set your credentials at Email-Classification-Bot/dist/config.json

 2. Create and Connect to a local MySQL database named "email_classifier"

 3. Execute Email-Classification-Bot/dist/main.exe

 --------------------------------------------------------------------------------------------------------

# Advanced Features I Learned during this project

- OAuth2 Authentication: For secure access to Gmail or other providers using modern security practices.

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

  - QR Code Detection: pyzbar

  - Database: MySQL

Hosting & Building

  - Email Provider Integration: Gmail API (OAuth2) or direct IMAP access (for any email provider)

  - Build: PyInstaller 
    
 --------------------------------------------------------------------------------------------------------

 # Project Roadmap

 This project was made as a personal projects to help me manage my emails. The whole project was made in 6 sprints, each a week long.

### WEEK 1: Project Setup & Email Access
  
- Goal: Set up project structure and read emails from your inbox.

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

Tech: email.message, email.utils

4. Store Raw Email Metadata in Database (3h)
   
Set up MySQL database.

Tech: MySQL

Store: subject, from, to, date, body, uid


### WEEK 2: Classification Engine
  
- Goal: Implement basic keyword and metadata-based classification.

Tasks:
1. Setup Keyword Classification Module (3h)
   
Create a dictionary of keyword categories (e.g., bills, subscriptions, alerts).

Use string matching and re for regex-based keyword scans.

2. Implement Rule-Based Classifier Function (3h)
   
Assign categories based on: Subject, Sender address, Body keywords

Tech: Python logic + re, json, logging

3. Store Classification Results in Database (3h)
   
Add category column to DB schema.

Log confidence and triggered keyword.

4. Test Classifier on 10 Sample Emails (3h)
   
Build unit tests and mock emails.

Tech: pytest, unittest.mock

### WEEK 3: QR Code and Attachment Handling

- Goal: Detect and decode QR codes from email images and PDF attachments.

Tasks:

1. Download Attachments from Emails (3h)

Parse emails with .get_payload() and save attachments.

2. Detect & Decode QR Codes from Images (3h)
   
Use pyzbar to scan images for QR codes.

Output decoded text or URLs.

3. Extract QR Codes from PDFs (3h)
   
Convert PDF pages to images using PyMuPDF or pdf2image, then scan.

Tech: PyMuPDF, PIL, pyzbar

4. Classify Emails Containing QR Codes (3h)
   
Tag email as “QR Detected” and extract code contents.

Update DB table with qr_data field.

###  WEEK 4: Automation & Building
  
- Goal: Automate the bot and convert to a executable.

Tasks:

1. Write a Scheduled Script (3h)
   
Use schedule or APScheduler to check emails every X minutes.

Tech: schedule, threading, time

2. Prepare for configurations do build (1h)
   
Move credentials/config to json

4. Set Up the executable (3h)

Build the project into a .exe for easier download

Tech: PyInstaller

 --------------------------------------------------------------------------------------------------------

 # Possible errors
 
  - Dll dependency missing
      
    libzbar-64.dll requires MSVCR120.dll to load.  
    If this DLL is missing, Windows cannot load libzbar-64.dll, and you get the error in Python.  
  
    Solution: Download and Install the Visual C++ 2013 Redistributable (x64):  

    1. Go to the official Microsoft page: https://www.microsoft.com/en-us/download/details.aspx?id=40784
     
  - Authentication failed while trying to login with IMAP
      
    Google blocks "less secure apps" by default, so now Gmail requires an App Password for IMAP access, even if you don’t have 2FA, for most accounts.
    
    Solution: Enable 2FA and use a App Password ganerated in your google account management area  
  
  - Poppler download missing

    You need to externally download Poppler 
    
    Solution: Install Poppler for Windows  

     1. Download the latest Poppler binary from 
      https://github.com/oschwartz10612/poppler-windows/releases/  
       Extract the zip file to a folder, e.g., C:\poppler.

     2. Add Poppler to your PATH:
       Open Windows "Environment Variables".  
       Edit the PATH variable and add the path to the bin folder inside your Poppler directory, e.g., C:\poppler\bin.


