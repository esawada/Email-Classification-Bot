# email_bot/database.py

from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URL
from datetime import datetime

Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

class EmailRecord(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    subject = Column(Text)
    sender = Column(String(256))
    date = Column(String(128))
    body = Column(Text)
    category = Column(String(64))
    keyword = Column(String(64))
    qr_data = Column(JSON)
    received_at = Column(DateTime, default=datetime.utcnow)

def save_email_record(email_data, category, keyword, qr_data):
    session = Session()
    record = EmailRecord(
        subject=email_data["subject"],
        sender=email_data["from"],
        date=email_data["date"],
        body=email_data["body"],
        category=category,
        keyword=keyword,
        qr_data=qr_data
    )
    session.add(record)
    session.commit()
    session.close()

def init_db():
    Base.metadata.create_all(engine)
