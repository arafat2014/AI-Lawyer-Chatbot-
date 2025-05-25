from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

# Step 1: Setup LLM (DeepSeek R1 via Groq)
llm_model=ChatGroq(model="deepseek-r1-distill-llama-70b")

# Step 2: Retrieve Documents
def retrieve_docs(query: str):
    """
    Perform similarity search on the vector database using the user query.
    """
    return faiss_db.similarity_search(query)

def get_context(documents) -> str:
    """
    Combine content from relevant documents into a single context string.
    """
    return "\n\n".join(doc.page_content for doc in documents)
