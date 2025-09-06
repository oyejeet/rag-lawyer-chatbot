# RAG Lawyer Chatbot

A **PDF-based RAG (Retrieval-Augmented Generation) chatbot** that answers legal questions using uploaded documents. It leverages **DeepSeek R1** as the LLM and **FAISS** as the vector store for semantic search.

---

### Features

- Upload any PDF document and use it as a knowledge base.  
- Ask legal questions in natural language.  
- RAG pipeline retrieves relevant document chunks and provides answers based on context.  
- Interactive chat interface using **Streamlit**.

---

### Installation

1. Clone the repository:

```bash
git clone https://github.com/oyejeet/rag-lawyer-chatbot.git
cd RAG-Lawyer-ChatBot

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3.	Install dependencies:

pip install -r requirements.txt

4.	Add your DeepSeek or Gemini API keys to .env if required:

DEEPSEEK_API_KEY=your_api_key_here