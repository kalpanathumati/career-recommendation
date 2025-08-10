from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini chat model
chat = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY,
    temperature=0.7
)

def get_recommendations(user_profile: dict) -> str:
    """
    Uses Gemini to generate personalized career recommendations.

    Args:
        user_profile (dict): Contains user's name, education, interests, skills, goals, etc.

    Returns:
        str: Gemini's AI-generated career guidance
    """

    prompt = f"""
You are a career guidance assistant AI.

Based on the following student profile, suggest the top 3–5 best-fit career paths.
Explain why each is a good fit, and suggest educational paths to reach them.

Student Profile:
- Name: {user_profile.get("name", "N/A")}
- Education Level: {user_profile.get("education", "N/A")}
- Subjects of Interest: {", ".join(user_profile.get("interests", []))}
- Skills: {", ".join(user_profile.get("skills", []))}
- Future Goals: {user_profile.get("quiz_result", "Not specified")}
- Selected Path: {user_profile.get("selected_path", "N/A")}

Return your answer in clear, friendly language with bullet points.
"""

    try:
        response = chat.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"❌ Gemini error: {str(e)}"
