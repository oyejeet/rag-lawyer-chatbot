# Step 1: Setting up LLM using Deepseek R1 with groq

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm_model = ChatGroq(model='llama-3.3-70b-versatile')

# Step2 : Retreiving docs

def retreive_docs(query):
  return faiss_db.similarity_search(query)

# print(retreive_docs('If a government forbids the right to assemble peacefully which articles are violated and why?'))

def get_context(documents):
  context = "\n\n".join([doc.page_content for doc in documents])
  return context

# Step 3 : Answer Question

custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})
  
# question="If a government forbids the right to assemble peacefully which articles are violated and why?"
# retrieved_docs=retreive_docs(question)
# print("AI Lawyer: ",answer_query(documents=retrieved_docs, model=llm_model, query=question).content)