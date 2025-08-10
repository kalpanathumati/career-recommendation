import os
import requests

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def query_gemini(prompt: str) -> str:
    """
    Query Gemini 2.0 Flash API for a generated response.
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
    
    # DEBUG: print status and response for troubleshooting
    print(f"HTTP status: {response.status_code}")
    print(f"Response content: {response.text}")

    # Instead of raise_for_status, handle error gracefully
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    
    result = response.json()
    return result.get("candidates", [{}])[0].get("content", "")
