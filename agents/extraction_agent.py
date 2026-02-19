import re

def extract_invoice_entities(text):

    invoice_id = re.findall(r'INV-\d+', text)
    amount = re.findall(r'\d{1,3},?\d{0,3}\s?INR', text)
    due_date = re.findall(r'\d{1,2}\s[A-Za-z]{3}\s\d{4}', text)

    return {
        "invoice_id": invoice_id[0] if invoice_id else None,
        "amount": amount[0] if amount else None,
        "due_date": due_date[0] if due_date else None
    }
