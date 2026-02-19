import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from groq import Groq

load_dotenv()
print("DEBUG: Loaded GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(context):
    if isinstance(context, str):
        # Agar string aa raha hai, usko dict me convert kar do
        context = {
            "urgency": "Unknown",
            "department": "Finance",
            "entities": None,
            "rule": context  # string treat as 'rule'
        }


    try:
        # ✅ Check API Key
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Groq‑supported LLM model
            messages=[
                { "role": "system",
                  "content": "You are a finance support AI." },
                { "role": "user",
                  "content": f"""
Urgency: {context.get('urgency')}
Department: {context.get('department')}
Entities: {context.get('entities')}
Finance Rule: {context.get('rule')}

Generate a professional finance response.
"""}
            ]
        )

        # Extract the generated text
        return response.choices[0].message.content

    except Exception as e:
        print("❌ Groq API Error:", e)
        print("⚠️ Using fallback")

        # Fallback static reply
        return f"""
We have received your request.

Priority Level: {context.get('urgency')}
Department Assigned: {context.get('department')}

Our team is reviewing your financial concern.
"""