import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Load Gemini API key from environment variable for security
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Please set the GEMINI_API_KEY environment variable.")

def query_gemini(prompt: str) -> str:
    """
    Sends a prompt to Gemini AI via LangChain and returns the response text.
    """
    llm = ChatOpenAI(model="gemini-pro", api_key=API_KEY, temperature=0.7)
    response = llm([HumanMessage(content=prompt)])
    return response.content
