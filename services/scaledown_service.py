import requests
from config import (
    SCALEDOWN_API_KEY,
    SCALEDOWN_COMPRESS_URL,
    SCALEDOWN_CHAT_URL
)


headers = {
    "Authorization": f"Bearer {SCALEDOWN_API_KEY}",
    "Content-Type": "application/json"
}


def compress_menu_once(raw_text):
    payload = {
        "text": raw_text,
        "compression_level": "high"
    }

    try:
        response = requests.post(
            SCALEDOWN_COMPRESS_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            return response.json().get("compressed_text", raw_text)
        else:
            return raw_text

    except:
        return raw_text


def chat_with_menu(compressed_menu, user_query):
    payload = {
        "model": "scaledown-chat",
        "messages": [
            {
                "role": "system",
                "content": "You are an intelligent restaurant assistant. Use the compressed menu to answer accurately."
            },
            {
                "role": "user",
                "content": f"Menu:\n{compressed_menu}\n\nUser Question:\n{user_query}"
            }
        ]
    }

    try:
        response = requests.post(
            SCALEDOWN_CHAT_URL,
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"API Error: {response.status_code}"

    except Exception as e:
        return f"Connection Error: {str(e)}"
