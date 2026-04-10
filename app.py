from flask import Flask, render_template, request, jsonify
from rag_engine import search_faq
from gemini import ask_gemini

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user = request.json["message"]

    answer = search_faq(user)

    if answer:
        return jsonify({"reply": answer})

    ai_answer = ask_gemini(user)

    return jsonify({"reply": ai_answer})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)