intents = {
    "reset_password": ["reset password", "forgot password"],
    "order_status": ["where is my order", "track order"],
    "refund": ["refund policy", "refund"],
    "contact_support": ["contact support", "help"]
}

def detect_intent(text):

    text = text.lower()

    for intent, phrases in intents.items():
        for phrase in phrases:
            if phrase in text:
                return intent

    return "unknown"