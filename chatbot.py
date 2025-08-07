from translator import Translator
from faq_engine import FAQEngine

class Chatbot:
    def __init__(self):
        self.translator = Translator()
        self.faq_engine = FAQEngine()

    def get_response(self, user_input):
        translated_input, detected_lang_code = self.translator.translate_to_english(user_input)
        answer_in_english = self.faq_engine.get_answer(translated_input)
        final_response = self.translator.translate_from_english(answer_in_english, detected_lang_code)
        return final_response
