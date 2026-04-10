import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

with open("data/faq.json") as f:
    data = json.load(f)

# FIX
if "faqs" in data:
    data = data["faqs"]

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

model = SentenceTransformer("all-MiniLM-L6-v2")

question_embeddings = model.encode(questions)

def search_faq(query):

    query_embedding = model.encode([query])

    scores = cosine_similarity(query_embedding, question_embeddings)

    best_match = np.argmax(scores)

    if scores[0][best_match] > 0.5:
        return answers[best_match]

    return None