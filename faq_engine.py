import json
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

class FAQEngine:
    def __init__(self):
        # Use MiniLM for sentence embeddings
        model_name = 'sentence-transformers/all-MiniLM-L6-v2'
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

        with open("guvi_faq.json", "r", encoding="utf-8") as f:
            self.faq_data = json.load(f)

        self.questions = [item["question"] for item in self.faq_data]
        self.answers = [item["answer"] for item in self.faq_data]
        self.question_embeddings = self._encode(self.questions)

    def _mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size())
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
            input_mask_expanded.sum(1), min=1e-9
        )

    def _encode(self, texts):
        encoded_input = self.tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        return self._mean_pooling(model_output, encoded_input['attention_mask'])

    def get_answer(self, user_question):
        question_embedding = self._encode([user_question])[0]
        similarities = F.cosine_similarity(
            question_embedding.unsqueeze(0), self.question_embeddings
        )
        best_match_idx = torch.argmax(similarities).item()
        return self.answers[best_match_idx]
