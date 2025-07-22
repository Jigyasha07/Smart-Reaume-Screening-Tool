import pytesseract
from PIL import Image
import pdfplumber

# ✅ Tell pytesseract where Tesseract is installed

def extract_text_from_pdf_or_image(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
            return text
    elif file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(file)
        return pytesseract.image_to_string(image)
    else:
        return "Unsupported file format"
