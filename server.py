from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion detection")


@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return jsonify({
            'error': 'No text provided',
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0,
            'dominant_emotion': 'unknown'
        }), 400
    
    response = emotion_detector(text_to_analyze)
    scores = {
        'anger': response.get('anger', 0),
        'disgust': response.get('disgust', 0),
        'fear': response.get('fear', 0),
        'joy': response.get('joy', 0),
        'sadness': response.get('sadness', 0),
    }
    dominant_emotion = max(scores, key=scores.get)

    return jsonify({
        'anger': scores['anger'],
        'disgust': scores['disgust'],
        'fear': scores['fear'],
        'joy': scores['joy'],
        'sadness': scores['sadness'],
        'dominant_emotion': dominant_emotion
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)