from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    def __init__(self):
        self.model_name = "facebook/nllb-200-distilled-600M"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, use_fast=False)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

        self.language_map = {
            "English": "eng_Latn",
            "Hindi": "hin_Deva",
            "Tamil": "tam_Taml",
            "Telugu": "tel_Telu",
            "Bengali": "ben_Beng",
            "Kannada": "kan_Knda",
            "Malayalam": "mal_Mlym",
            "Marathi": "mar_Deva",
            "Gujarati": "guj_Gujr",
            "Punjabi": "pan_Guru",
            "Urdu": "urd_Arab"
        }

    def translate(self, text: str, src_lang: str, tgt_lang: str) -> str:
        if src_lang not in self.language_map or tgt_lang not in self.language_map:
            raise ValueError("Unsupported language")

        src_code = self.language_map[src_lang]
        tgt_code = self.language_map[tgt_lang]

        self.tokenizer.src_lang = src_code
        encoded = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(
            **encoded,
            forced_bos_token_id=self.tokenizer.convert_tokens_to_ids(tgt_code)
        )
        return self.tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
