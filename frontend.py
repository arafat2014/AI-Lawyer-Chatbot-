from rag_pipeline import answer_query, retrieve_docs, llm_model
import streamlit as st

# --- Page config ---
st.set_page_config(page_title="AI Legal Assistant", page_icon="⚖️", layout="centered")

st.title("⚖️ AskLex R1 – Your AI Legal Assistant")

# --- Upload section ---
st.markdown("### 📄 Upload a Legal PDF")
uploaded_file = st.file_uploader(
    "Drop your legal document here...",
    type="pdf",
    help="Upload a legal contract, declaration, or policy document."
)

st.markdown("---")

# --- Chat section ---
st.markdown("### 💬 Ask a Question")
user_query = st.text_area(
    label="What's on your mind?",
    placeholder="e.g., What rights are mentioned in this document?",
    height=100,
    label_visibility="collapsed"
)

submit_question = st.button("🧠 Ask the AI Lawyer")

# --- Chat logic ---
if submit_question:
    if uploaded_file and user_query.strip():
        with st.spinner("🧠 Thinking..."):
            st.chat_message("user").markdown(f"**You:** {user_query}")
            docs = retrieve_docs(user_query)
            answer = answer_query(documents=docs, model=llm_model, query=user_query)
            st.chat_message("assistant").markdown(f"**AI Lawyer:** {answer}")
    elif not uploaded_file:
        st.error("❗ Please upload a PDF document before asking a question.")
    else:
        st.warning("⚠️ Please enter a valid question.")
