from services.llm_service import generate_response

def draft_reply(context):

    ticket_text = context.get("ticket_text", "")
    urgency = context.get("urgency", "")
    department = context.get("department", "")
    entities = context.get("entities", {})
    finance_rule = context.get("finance_rule", "")

    prompt = f"""
You are an AI Finance Support Assistant.

A user has submitted a financial issue ticket.

Ticket Details:
--------------
Ticket Text: {ticket_text}

Urgency Level: {urgency}
Department: {department}

Extracted Entities:
{entities}

Relevant Finance Rule:
{finance_rule}

Your task:
1. Understand the issue
2. Use the finance rule if applicable
3. Generate a helpful professional response
4. Adjust tone based on urgency
5. Provide resolution guidance

Response Guidelines:
- Be polite
- Be concise
- Be professional
- Give next steps if needed
- If urgent → sound proactive
- If low priority → sound calm

Generate a dynamic human-like reply.
"""

    response = generate_response(prompt)

    return response
