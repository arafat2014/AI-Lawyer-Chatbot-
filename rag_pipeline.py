from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Step 1: Setup LLM (DeepSeek R1 via Groq)
llm_model=ChatGroq(model="deepseek-r1-distill-llama-70b")

