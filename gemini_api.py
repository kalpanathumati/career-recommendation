from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY in the .env file.")

chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

def query_gemini(prompt: str) -> str:
    try:
        response = chat.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"❌ Gemini API error: {str(e)}"
