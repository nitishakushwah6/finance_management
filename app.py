import streamlit as st
import requests

# ---------- Page Config ----------
st.set_page_config(
    page_title="Finance Triage Agent",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Finance Triage Agent")
st.write("Upload finance documents or type your query and get AI-assisted triage response.")

# ---------- File Upload ----------
uploaded_file = st.file_uploader("Upload PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

# ---------- Text Query ----------
user_query = st.text_input("Or enter your query:")

# ---------- Submit Button ----------
if st.button("Submit"):
    if uploaded_file:
        # Save file temporarily
        with open(f"temp_{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("http://127.0.0.1:8000/process_file", files=files)
        st.success("✅ File processed")
        st.text_area("AI Response:", value=response.json()["response"], height=250)
    
    elif user_query:
        # Send query only
        payload = {"text": user_query}
        response = requests.post("http://127.0.0.1:8000/triage", json=payload)
        st.text_area("AI Response:", value=response.text, height=250)
    
    else:
        st.warning("Please upload a file or type a query!")
