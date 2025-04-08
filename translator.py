from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

def translate_to_english(text):
    return translator(text, max_length=1000)[0]['translation_text']
