
from flask import Flask, request, jsonify, render_template
from app.model import load_model, predict
from app.database import add_article, get_recent_articles

app = Flask(__name__)

# Load the trained model and vectorizer
model, vectorizer = load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction, probability = predict(text, model, vectorizer)
    add_article(text, prediction, probability)

    return jsonify({"prediction": prediction, "probability": probability})

@app.route('/results', methods=['GET'])
def results():
    articles = get_recent_articles()
    return jsonify({"articles": articles})

if __name__ == '__main__':
    app.run(debug=True)
