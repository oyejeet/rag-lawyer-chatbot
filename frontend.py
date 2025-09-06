from rag_pipeline import answer_query, retreive_docs, llm_model
# Step 1: Setup PDF upload functionality

import re
import streamlit as st

# Utility function to strip <think> ... </think>
def clean_response(text: str) -> str:
  return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

uploaded_file = st.file_uploader(
  "Upload Pdf",
  type="pdf",
  accept_multiple_files = False
)

# Step 2: Chatbot Skeleton (Question & Answer)

user_query = st.text_area("Enter your prompt: ", height=150, placeholder="Ask anything")

ask_question = st.button("Ask AI Lawyer")

if ask_question:
  if uploaded_file:
    st.chat_message("user").write(user_query)
    
    # RAG pipeline
    retrieved_docs=retreive_docs(user_query)
    response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
    
    cleaned_response = clean_response(response.content)
    st.chat_message("AI Lawyer").write(cleaned_response)
  
  else:
    st.error("Kindly upload any pdf file first")


