# Step1: Upload and load Raw pdfs

from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

pdfs_directory= '/pdfs'
def upload_pdf(file):
  with open(pdfs_directory + file.name, 'wb') as f:
    f.write(file.getbuffer())


def load_pdf(file_path):
  loader=PDFPlumberLoader(file_path)
  documents= loader.load()
  return documents

file_path = "/Users/indrajeetsinghbava/Desktop/RAG-Lawyer-ChatBot/pdfs/universal_declaration_of_human_rights.pdf"
documents = load_pdf(file_path)
print(len(documents))

# Step2: Create Chunks

def create_chunks(documents):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap= 200,
    add_start_index = True
  )
  text_chunks = text_splitter.split_documents(documents)
  return text_chunks
text_chunks = create_chunks(documents)

# Step3: Setup Embeddings model, (using deepseek R1 with Ollama) 

ollama_model_name = 'deepseek-r1:1.5b'

def get_embedding_model(ollama_model_name):
  embeddings= OllamaEmbeddings(model= ollama_model_name)
  return embeddings

# Step4: Index documents, Store embeddings in Vector Stores

FAISS_DB_PATH = "vectorStore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, get_embedding_model(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)