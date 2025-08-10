from gemini_api import query_gemini

def get_recommendations(user_profile: dict) -> str:
    prompt = f"""
You are a helpful career guidance AI.

Profile:
- Name: {user_profile.get('name')}
- Education: {user_profile.get('education')}
- Interests: {', '.join(user_profile.get('interests', []))}
- Skills: {', '.join(user_profile.get('skills', []))}
- Quiz Result: {user_profile.get('quiz_result', 'None')}
- Selected Path: {user_profile.get('selected_path')}

Suggest the top 3–5 fitting careers, reasons, and next education steps.
"""
    return query_gemini(prompt)
