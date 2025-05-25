# Step 1: Add functionality to upload PDF files
import streamlit as st

uploaded_file = st.file_uploader("Upload PDF",
                                 type="pdf",
                                 accept_multiple_files=False)

# Step 2: Set up the chatbot's question-answer logic
user_query = st.text_area(
    label="💬 What's on your mind?",
    placeholder="Type your question here...",
    height=120
)




