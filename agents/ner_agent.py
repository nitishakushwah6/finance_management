import re

def extract_entities(text):
    invoice = re.findall(r'INV-\d+', text)
    amount = re.findall(r'\₹?\d+', text)
    date = re.findall(r'\d{2}/\d{2}/\d{4}', text)

    return {
        "invoice": invoice,
        "amount": amount,
        "date": date
    }
