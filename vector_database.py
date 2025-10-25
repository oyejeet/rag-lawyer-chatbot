# Step1: Upload and load Raw pdfs

from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

import os
pdfs_directory = os.path.join(os.getcwd(), 'pdfs')
def upload_pdf(file):
  file_path = os.path.join(pdfs_directory, file.name)
  with open(file_path, 'wb') as f:
    f.write(file.getbuffer())


def load_pdf(file_path):
  loader=PDFPlumberLoader(file_path)
  documents= loader.load()
  return documents

# Check if PDF exists before loading
file_path = os.path.join(pdfs_directory, "universal_declaration_of_human_rights.pdf")
if os.path.exists(file_path):
    documents = load_pdf(file_path)
    print(f"Loaded {len(documents)} documents from PDF")
else:
    print("PDF file not found, creating empty documents list")
    documents = []

# Step2: Create Chunks

def create_chunks(documents):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap= 200,
    add_start_index = True
  )
  text_chunks = text_splitter.split_documents(documents)
  return text_chunks
if documents:
    text_chunks = create_chunks(documents)
    
    # Step3: Setup Embeddings model (using OpenAI embeddings for cloud deployment)
    def get_embedding_model():
        embeddings = OpenAIEmbeddings()
        return embeddings
    
    # Step4: Index documents, Store embeddings in Vector Stores
    FAISS_DB_PATH = "vectorStore/db_faiss"
    faiss_db = FAISS.from_documents(text_chunks, get_embedding_model())
    faiss_db.save_local(FAISS_DB_PATH)
    print("Vector database created successfully")
else:
    print("No documents to process, creating empty vector database")
    # Create an empty FAISS database
    from langchain_community.vectorstores import FAISS
    from langchain_openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()
    faiss_db = FAISS.from_texts([""], embeddings)
    FAISS_DB_PATH = "vectorStore/db_faiss"
    faiss_db.save_local(FAISS_DB_PATH)