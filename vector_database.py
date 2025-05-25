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
file_path ='udhr_booklet_en_web.pdf'
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
print("Chunks count: ", len(text_chunks))