💰 Finance AI Triage System

An AI-powered Finance Support Automation System that helps organizations automatically process finance-related tickets by extracting information from documents, understanding the issue, checking finance policies, and generating intelligent responses.

This system reduces manual workload, speeds up resolution time, and ensures consistent financial support.

🚀 Features

✅ Upload PDF / Image Finance Documents
✅ OCR-based Text Extraction
✅ AI-based Ticket Classification
✅ Entity Extraction (Invoice ID, Payment Info, etc.)
✅ Finance Rule Verification via Web Scraping
✅ AI-generated Professional Response
✅ Streamlit Frontend Interface
✅ FastAPI Backend
✅ MongoDB Ticket Storage

🧠 AI Capabilities Used

LLM-based Response Generation

NLP Classification

Named Entity Recognition

Rule-based Financial Policy Checking

Intelligent Triage

🏗️ Tech Stack
Layer	Technology
Frontend	Streamlit
Backend	FastAPI
AI Orchestration	LangChain
LLM Provider	Groq API
OCR	Tesseract
Web Scraping	BeautifulSoup
Database	MongoDB
NLP	Scikit-learn
📂 Project Structure
finance_management/
│
├── agents/
│   ├── classification_agent.py
│   ├── ner_agent.py
│   └── response_agent.py
│
├── services/
│   ├── ocr_service.py
│   ├── scraping_service.py
│   ├── db_service.py
│   └── llm_service.py
│
├── uploads/
│
├── main.py
├── app.py
├── .env
└── README.md

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/finance-ai-triage.git
cd finance-ai-triage

2️⃣ Install Requirements
pip install fastapi uvicorn streamlit pytesseract pdf2image pillow pymongo requests beautifulsoup4 scikit-learn python-dotenv langchain groq

3️⃣ Install Tesseract OCR

Download from:

👉 https://github.com/tesseract-ocr/tesseract

After installing, update path inside:

services/ocr_service.py

4️⃣ Add API Key

Create .env file

GROQ_API_KEY=your_api_key_here
MONGO_URI=your_mongodb_connection_string

▶️ Running the Project
Start Backend
python -m uvicorn main:app --reload --port 8000

Start Frontend
python -m streamlit run app.py

🧪 Testing
Sample Query
Payment for invoice #456 is pending for 10 days.


OR upload invoice PDF.

🔄 System Workflow
User uploads finance document or enters query

OCR extracts text

AI classifies urgency & department

Entities extracted

Finance rules fetched via web scraping

LLM generates response

Ticket stored in database

📌 Use Cases

Payment Issue Handling

Invoice Disputes

Reimbursement Queries

Financial Document Verification
