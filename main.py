from services.ocr_service import extract_text_from_pdf, extract_text_from_image
from agents.classification_agent import classify
from agents.ner_agent import extract_entities
from fastapi import FastAPI,UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.scraping_service import check_finance_rule
from agents.response_agent import draft_reply
from services.db_service import save_ticket
import os
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ya "http://localhost:8501" agar Streamlit specific ho
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/triage")
def triage(query: dict):
    text = query.get("text", "")
    # call your LLM / fallback here
    response = draft_reply({"text": text})
    return {"response": response}

@app.post("/process_file")
def process_file(file: UploadFile = File(...)):
    if not file:
        return {"response": "No file uploaded!"}

    # Read bytes
    content = file.file.read()
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(content)

    # OCR
    if temp_file.endswith(".pdf"):
        text = extract_text_from_pdf(temp_file)
    else:
        text = extract_text_from_image(temp_file)

    # Classification + NER + Web scraping
    urgency, department = classify(text)
    entities = extract_entities(text)
    finance_rule = check_finance_rule()

    context = {
        "ticket_text": text,
        "urgency": urgency,
        "department": department,
        "entities": entities,
        "finance_rule": finance_rule
    }

    response_text = draft_reply(context)

    return {"response": response_text}


def process_ticket(input_text=None, file=None):

    # ---------- STEP 1 : GET TEXT ----------
    if file:
        if file.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file)
        elif file.lower().endswith((".png", ".jpg", ".jpeg")):
            text = extract_text_from_image(file)
        else:
            print("❌ Unsupported file format")
            return
    else:
        text = input_text

    if not text or text.strip() == "":
        print("❌ No text extracted!")
        return

    print("\n================ OCR OUTPUT ================\n")
    print(text)


    # ---------- STEP 2 : CLASSIFICATION ----------
    urgency, department = classify(text)

    print("\n================ CLASSIFICATION ================\n")
    print("Urgency:", urgency)
    print("Department:", department)


    # ---------- STEP 3 : ENTITY EXTRACTION ----------
    entities = extract_entities(text)

    print("\n================ ENTITY EXTRACTION ================\n")
    print(entities)


    # ---------- STEP 4 : WEB SCRAPING ----------
    finance_rule = check_finance_rule()

    print("\n================ FINANCE RULE (SCRAPED) ================\n")
    print(finance_rule)


    # ---------- STEP 5 : AI RESPONSE (OPENAI POWERED) ----------
    context = {
        "ticket_text": text,
        "urgency": urgency,
        "department": department,
        "entities": entities,
        "finance_rule": finance_rule
    }

    response = draft_reply(context)

    print("\n================ AI RESPONSE ================\n")
    print(response)


    # ---------- STEP 6 : SAVE ----------
    save_ticket({
        "text": text,
        "urgency": urgency,
        "department": department,
        "entities": entities,
        "finance_rule": finance_rule,
        "response": response
    })

    print("\n✅ Ticket saved successfully!")

    return response



# ================= ENTRY POINT =================

if __name__ == "__main__":

    print("\n🚀 Finance AI Ticket System Started...\n")

    uploads_folder = "uploads"

    if not os.path.exists(uploads_folder):
        print("❌ uploads folder not found!")
        exit()

    files = os.listdir(uploads_folder)

    if len(files) == 0:
        print("❌ No files found inside uploads folder!")
        exit()

    print("📂 Files found:", files)

    # Process ALL files (better than only first)
    for file in files:
        file_path = os.path.join(uploads_folder, file)
        print("\n📄 Processing file:", file_path)
        process_ticket(file=file_path)
