import pytesseract
from PIL import Image
from pdf2image import convert_from_path


# Tell python where tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\aayus\Downloads\Release-25.12.0-0\poppler-25.12.0\Library\bin"


# ---------- IMAGE OCR ----------
def extract_text_from_image(file_path):
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    
    except Exception as e:
        return f"OCR Image Error: {str(e)}"



# ---------- PDF OCR ----------
def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(
            pdf_path,
            poppler_path=POPPLER_PATH   # ⭐ THIS WAS MISSING
        )

        full_text = ""

        for page in pages:
            text = pytesseract.image_to_string(page)
            full_text += text + "\n"

        return full_text.strip()

    except Exception as e:
        return f"OCR PDF Error: {str(e)}"
