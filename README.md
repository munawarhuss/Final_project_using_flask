# Emotion Detection Service

A Flask-based web service that detects emotions in text using Watson NLP services.

## Features

- Emotion analysis of provided text
- Returns scores for: anger, disgust, fear, joy, and sadness
- Identifies the dominant emotion
- RESTful API endpoint
- Web interface for testing

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python server.py
```

3. Access the service:
- Web interface: http://localhost:8000
- API endpoint: http://localhost:8000/emotionDetector?textToAnalyze=your+text+here

## API Usage

### GET /emotionDetector

Analyzes the emotional content of provided text.

**Parameters:**
- `textToAnalyze` (required): Text to analyze for emotional content

**Example Request:**
```
GET http://localhost:8000/emotionDetector?textToAnalyze=I%20am%20happy
```

**Success Response:**
```json
{
    "anger": 0.031361,
    "disgust": 0.002157,
    "fear": 0.007221,
    "joy": 0.788140,
    "sadness": 0.007967,
    "dominant_emotion": "joy"
}
```

**Error Response:**
```json
{
    "error": "No text provided",
    "anger": 0,
    "disgust": 0,
    "fear": 0,
    "joy": 0,
    "sadness": 0,
    "dominant_emotion": "unknown"
}
```

## Development

- Python files use `autopep8` style
- Line endings are normalized via `.gitattributes`
- Flask debug mode is disabled by default
