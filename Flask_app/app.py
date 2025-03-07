from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Text input is required"}), 400

    text = data["text"]
    sentiment_score = analyzer.polarity_scores(text)["compound"]

    if sentiment_score >= 0.05:
        sentiment = "positive"
    elif sentiment_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)
