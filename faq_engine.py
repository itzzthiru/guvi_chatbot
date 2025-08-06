import json
import os
from sentence_transformers import SentenceTransformer, util

class FAQEngine:
    def __init__(self, faq_path="guvi_faq.json"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.faqs = self.load_faqs(faq_path)
        self.questions = [item["question"] for item in self.faqs]
        self.question_embeddings = self.model.encode(self.questions, convert_to_tensor=True)

    def load_faqs(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"FAQ file not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_answer(self, user_query, threshold=0.7):
        query_embedding = self.model.encode(user_query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.question_embeddings)[0]
        best_idx = scores.argmax().item()
        best_score = scores[best_idx].item()

        if best_score >= threshold:
            return self.faqs[best_idx]["answer"]
        return None

# ✅ Optional test
if __name__ == "__main__":
    engine = FAQEngine()
    q = "What does GUVI do?"
    print("Q:", q)
    print("A:", engine.get_answer(q))
