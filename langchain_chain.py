from gemini_api import query_gemini

def get_recommendations(user_data: dict) -> str:
    prompt = f"""
    Given the user's data: {user_data}, provide a personalized career recommendation.
    Use clear, concise language.
    """
    try:
        response = query_gemini(prompt)
        return response
    except Exception as e:
        return f"Error generating recommendation: {e}"
