# app/preprocess.py

import re
import string

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(f"[{string.punctuation}]", "", text)  # Remove punctuation
    text = text.lower()
    return text
