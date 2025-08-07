from translator import Translator
from faq_engine import FAQEngine
from guvi_engine import GuviEngine

class Chatbot:
    def __init__(self):
        self.translator = Translator()
        self.faq_engine = FAQEngine()
        self.guvi_engine = GuviEngine()

    def ask(self, query, input_lang="English", output_lang="English"):
        print(f"[User] ({input_lang}):", query)

        # Step 1: Translate to English
        if input_lang != "English":
            query = self.translator.translate(query, input_lang, "English")

        # Step 2: Check FAQ
        faq_ans = self.faq_engine.get_answer(query)
        if faq_ans:
            result = faq_ans
        else:
            # Step 3: Try GUVI.txt
            guvi_ans = self.guvi_engine.get_best_match(query)
            result = guvi_ans if guvi_ans else "Sorry, I couldn’t find an answer."

        # Step 4: Translate back to output language
        if output_lang != "English":
            result = self.translator.translate(result, "English", output_lang)

        return result

# ✅ Test it!
if __name__ == "__main__":
    bot = Chatbot()
    q = "GUVI என்ன செய்கிறது?"  # Tamil input
    print("Bot:", bot.ask(q, input_lang="Tamil", output_lang="Tamil"))
