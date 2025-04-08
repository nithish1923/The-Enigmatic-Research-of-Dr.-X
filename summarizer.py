from transformers import pipeline
from rouge import Rouge

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
rouge = Rouge()

def summarize(text):
    summary = summarizer(text, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
    return summary

def evaluate_summary(reference, summary):
    return rouge.get_scores(summary, reference)
