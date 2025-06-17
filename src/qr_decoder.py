# import os
# import tempfile
# from email import message
# from PyPDF2 import PdfReader
# from PIL import Image
# from pdf2image import convert_from_bytes
# from pyzbar.pyzbar import decode
# from loguru import logger

# def process_attachments_for_qr(msg: message.Message):
#     qr_data = []

#     for part in msg.walk():
#         content_dispo = str(part.get("Content-Disposition", ""))
#         filename = part.get_filename()
#         if "attachment" in content_dispo and filename:
#             payload = part.get_payload(decode=True)

#             try:
#                 if filename.lower().endswith(".pdf"):
#                     qr_data.extend(decode_qr_from_pdf(payload))
#                 elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
#                     qr_data.extend(decode_qr_from_image(payload))
#             except Exception as e:
#                 logger.warning(f"Error processing {filename}: {e}")

#     return qr_data if qr_data else None

# def decode_qr_from_image(content):
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
#         tmp.write(content)
#         tmp_path = tmp.name
#     try:
#         image = Image.open(tmp_path)
#         return [d.data.decode("utf-8") for d in decode(image)]
#     finally:
#         os.unlink(tmp_path)

# def decode_qr_from_pdf(content):
#     images = convert_from_bytes(content)
#     results = []
#     for img in images:
#         results.extend([d.data.decode("utf-8") for d in decode(img)])
#     return results
