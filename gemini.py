import requests

API_KEY =""

def ask_gemini(question):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": question}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    print("Gemini response:", result)

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "AI could not answer."