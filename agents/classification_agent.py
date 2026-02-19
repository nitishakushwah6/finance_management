from ml.urgency_model import predict_urgency

def classify(text):
    urgency = predict_urgency(text)

    if "salary" in text.lower():
        dept = "Payroll"
    elif "invoice" in text.lower():
        dept = "Accounts Payable"
    else:
        dept = "General Finance"

    return urgency, dept
