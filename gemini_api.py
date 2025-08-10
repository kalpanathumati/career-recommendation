import os
import requests

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def query_gemini(prompt: str) -> str:
    """
    Calls Gemini 2.0 Flash API for text generation.
    """
    url = "https://generativelanguage.googleapis.com/v1beta2/models/chat-bison-001:generateMessage"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GOOGLE_API_KEY}"
    }
    
    data = {
        "prompt": {
            "messages": [
                {"content": prompt, "role": "user"}
            ]
        },
        "temperature": 0.7,
        "maxTokens": 512,
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    
    result = response.json()
    # Extract generated text from response JSON
    message = result.get("candidates", [{}])[0].get("content", "")
    return message
