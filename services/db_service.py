from pymongo import MongoClient
from config.settings import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def save_ticket(ticket):
    collection.insert_one(ticket)
    print("✅ Ticket saved in DB")