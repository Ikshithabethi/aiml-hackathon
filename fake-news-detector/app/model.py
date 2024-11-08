# app/model.py

import pickle
import numpy as np

def load_model():
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("tfidf.pkl", "rb") as tfidf_file:
        vectorizer = pickle.load(tfidf_file)
    return model, vectorizer

def predict(text, model, vectorizer):
    features = vectorizer.transform([text])
    probability = model.predict_proba(features)[0][1]
    prediction = "Real" if probability >= 0.5 else "Fake"
    return prediction, probability
