# chatbot.py
from translator import Translator
from faq_engine import FAQEngine
from guvi_engine import GuviEngine

class Chatbot:
    def __init__(self):
        self.translator = Translator()
        self.faq_engine = FAQEngine()
        self.guvi_engine = GuviEngine()

    def get_response(self, user_input: str, top_k: int = 3):
        """
        Returns a dictionary with FAQ answers and GUVI text results.
        """
        # Step 1: Translate input to English
        translated_input, lang_code = self.translator.translate_to_english(user_input)

        # Step 2: Search FAQ
        faq_results = self.faq_engine.get_answer(translated_input, top_k=top_k)

        # Step 3: Search GUVI text
        guvi_results = self.guvi_engine.search(translated_input, top_k=top_k)

        # Step 4: Translate answers back to user language
        final_faq = []
        for ans, score, src_q in faq_results:
            translated_back = self.translator.translate_from_english(ans, lang_code)
            final_faq.append((translated_back, score, src_q))

        final_guvi = []
        for para, score in guvi_results:
            translated_back = self.translator.translate_from_english(para, lang_code)
            final_guvi.append((translated_back, score))

        return {
            "detected_lang_code": lang_code,
            "translated_input": translated_input,
            "faq_answers": final_faq,
            "guvi_paragraphs": final_guvi
        }
