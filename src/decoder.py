import os
import tempfile
from email import message
from PIL import Image
from pdf2image import convert_from_bytes
from pyzbar.pyzbar import decode
from loguru import logger

# Boleto Digitable Line Regex (FEBRABAN standards)
# BOLETO_LINE_PATTERN = r'\b(\d{5}\.\d{5}\s\d{5}\.\d{6}\s\d{5}\.\d{6}\s\d{1}\s\d{14})\b'


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
                    for data in decode_from_pdf(payload):
                        if data[1] == "QRCODE" and data[0] not in qr_data:
                            qr_data.append(data[0])
                        elif data[0] not in boleto_data:
                            # matches = re.findall(BOLETO_LINE_PATTERN, data[0])
                            boleto_data.append(data[0])

                elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
                    for data in decode_from_image(payload):
                        if data[1] == "QRCODE" and data[0] not in qr_data:
                            qr_data.append(data[0])
                        elif data[0] not in boleto_data:
                            boleto_data.append(data[0])
            except Exception as e:
                logger.warning(f"Error processing {filename}: {e}")

    return qr_data, boleto_data if qr_data or boleto_data else None   

def decode_from_image(content):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    try:
        image = Image.open(tmp_path)
        return [[d.data.decode("utf-8") , d.type]for d in decode(image)]
    finally:
        os.unlink(tmp_path)

def decode_from_pdf(content):
    images = convert_from_bytes(content)
    results = []
    for img in images:
        results.extend([[d.data.decode("utf-8"), d.type] for d in decode(img)])
    return results

