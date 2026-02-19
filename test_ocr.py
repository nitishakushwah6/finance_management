from services.ocr_service import extract_text_from_pdf
from agents.extraction_agent import extract_invoice_entities

text = extract_text_from_pdf("invoice.pdf")

print("Extracted Text:")
print(text)

print("\nExtracted Entities:")
print(extract_invoice_entities(text))
