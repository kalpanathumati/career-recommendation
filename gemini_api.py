from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variable
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini Chat model
chat = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

def query_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini and return its response.
    """
    try:
        response = chat.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"
