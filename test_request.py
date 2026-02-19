import requests

# Backend URL
url = "http://127.0.0.1:8000/triage"

# Payload
payload = {
    "text": "Payment for invoice #123 pending"
}

# POST request
response = requests.post(url, json=payload)

# Print response
print(response.json())
