from PIL import Image
import pdfplumber
import easyocr
import numpy as np

reader = easyocr.Reader(['en'], gpu=False)
# Initialize EasyOCR reader (only once)



def extract_text_from_pdf_or_image(file):
    if file.name.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
            return text.strip()

    elif file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(file).convert('RGB')
        image_np = np.array(image)
        results = reader.readtext(image_np, detail=0)
        return '\n'.join(results).strip()

    else:
        return "Unsupported file format"
