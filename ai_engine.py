import requests

GEMINI_API_KEY = "AIzaSyCdd7Y-AK9zjFRZZ7jFmXmhow5S4HvuNX4"

def ask_ai(question):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts":[
                    {"text": question}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    try:
        answer = result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        answer = "Sorry, I could not generate an answer."

    return answer