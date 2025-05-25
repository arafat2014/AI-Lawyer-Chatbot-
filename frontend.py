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
submit_question = st.button("Ask the AI Lawyer")

if submit_question:

    if uploaded_file:

        # Display user's question in the chat
        st.chat_message("user").write(user_query)

        # Run RAG pipeline to fetch and respond
        docs = retrieve_docs(user_query)
        answer = answer_query(documents=docs, model=llm_model, query=user_query)

        # Display AI's response
        st.chat_message("AI Lawyer").write(answer)

    else:
        st.error("Please upload a PDF document before asking a question.")