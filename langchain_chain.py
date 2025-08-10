from gemini_api import query_gemini

def get_recommendations(user_profile: dict) -> str:
    """
    Generate AI-based career recommendations based on user profile.
    
    Args:
        user_profile (dict): Dictionary containing user details like education, interests, skills, quiz results.
    
    Returns:
        str: AI-generated recommendation text.
    """
    prompt = f"""
You are a career advisor AI.

User Profile:
- Education Level: {user_profile.get('education', 'N/A')}
- Interests: {', '.join(user_profile.get('interests', []))}
- Skills: {', '.join(user_profile.get('skills', []))}
- Quiz Result: {user_profile.get('quiz_result', 'N/A')}
- Selected Path: {user_profile.get('selected_path', 'N/A')}

Based on this, suggest the top 3 career options, explain why they fit the user, and include a confidence score (out of 100%) for each option.
Format your answer as a list with bullet points.
"""

    recommendations = query_gemini(prompt)
    return recommendations
