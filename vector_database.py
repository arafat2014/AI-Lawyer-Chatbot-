from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Define directory for PDF storage
PDF_DIRECTORY = 'pdfs/'

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())


def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

# Load a sample file
file_path ='universal_declaration_of_human_rights.pdf'
documents = documents = load_pdf(file_path)
#print(len(documents))

# Split into Chunks
def split_into_chunks(documents, chunk_size=1000, overlap=200):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        add_start_index=True
    )
    return splitter.split_documents(documents)

text_chunks = split_into_chunks(documents)
#print("Chunks count: ", len(text_chunks))

#Get Embedding Model (DeepSeek R1 via Ollama)
ollama_model_name = "deepseek-r1:14b"

def get_embedding_model(ollama_model_name):
    embeddings = OllamaEmbeddings(model=ollama_model_name)
    return embeddings

embedding_model = get_embedding_model(ollama_model_name)

#Store Embeddings in FAISS
FAISS_DB_PATH="vectorstore/db_faiss"
faiss_db=FAISS.from_documents(text_chunks, get_embedding_model(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)