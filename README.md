# RAG Lawyer Chatbot

A **PDF-based RAG (Retrieval-Augmented Generation) chatbot** that answers legal questions using uploaded documents. It leverages **Llama 3.3 70B** as the LLM, **OpenAI embeddings** for vectorization, and **FAISS** as the vector store for semantic search.

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
cd rag-lawyer-chatbot
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Ollama (required for embeddings):

```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows - download from https://ollama.ai/download
```

5. Pull the required Ollama model:

```bash
ollama pull deepseek-r1:1.5b
```

6. Set up your API keys:

```bash
# Edit the .env file and add your API keys
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### Running the Application

1. Start Ollama (if not already running):

```bash
ollama serve
```

2. Run the Streamlit application:

```bash
streamlit run frontend.py
```

3. Open your browser and go to `http://localhost:8501`

### Prerequisites

- **Python 3.8+**
- **Groq API Key** (get it from https://console.groq.com/)
- **OpenAI API Key** (get it from https://platform.openai.com/api-keys)
- **Internet connection** for API calls