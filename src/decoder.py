import os
import re
import tempfile
import pytesseract
from email import message
from PIL import Image
from pdf2image import convert_from_bytes
from pyzbar.pyzbar import decode
from loguru import logger

def process_attachments(msg: message.Message):
    qr_data = []
    boleto_data = []

    for part in msg.walk():
        content_dispo = str(part.get("Content-Disposition", ""))
        filename = part.get_filename()
        if "attachment" in content_dispo and filename:
            payload = part.get_payload(decode=True)

            try:
                if filename.lower().endswith(".pdf"):
                    qr_data.extend(decode_qr_from_pdf(payload))
                    boleto_data.extend(extract_boleto_from_pdf(payload))

                elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
                    qr_data.extend(decode_qr_from_image(payload))
            except Exception as e:
                logger.warning(f"Error processing {filename}: {e}")

    return qr_data, boleto_data if qr_data or boleto_data else None

def decode_qr_from_image(content):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        image = Image.open(tmp_path)
        return [d.data.decode("utf-8") for d in decode(image)]
    finally:
        os.unlink(tmp_path)

def decode_qr_from_pdf(content):
    images = convert_from_bytes(content)
    results = []
    for img in images:
        results.extend([d.data.decode("utf-8") for d in decode(img)])
    return results

# Boleto Digitable Line Regex (FEBRABAN standards)
BOLETO_LINE_PATTERN = r'\b(\d{5}\.\d{5}\s\d{5}\.\d{6}\s\d{5}\.\d{6}\s\d{1}\s\d{14})\b'

def extract_boleto_from_pdf(content):
    try:
        images = convert_from_bytes(content)
        full_text = ""
        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            full_text += f"\n[PAGE {i + 1}]\n{text}"
        matches = re.findall(BOLETO_LINE_PATTERN, full_text)
        if matches:
            logger.info(f"Boleto digitable line(s) found: {matches}")
        return matches if matches else None
    #still need to exclude doubles of the same boleto
    except Exception as e:
        logger.error(f"PDF text extraction failed: {e}")
        return ""
