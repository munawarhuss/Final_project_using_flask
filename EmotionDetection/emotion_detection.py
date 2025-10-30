import requests
import json

def emotion_detector (text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=my_obj, headers=header)
    
    if response.status_code == 200:
        # Convert the response text into a dictionary
        formatted_response = json.loads(response.text)
        
        # Extract the required set of emotions and their scores.
        # Assuming the standard nested structure: ['emotionPredictions'][0]['emotion']
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        
        scores = {
            'anger': emotion_data['anger'],
            'disgust': emotion_data['disgust'],
            'fear': emotion_data['fear'],
            'joy': emotion_data['joy'],
            'sadness': emotion_data['sadness'],
        }
        
        # Write the code logic to find the dominant emotion
        # Finds the key (emotion name) corresponding to the max value (score).
        dominant_emotion = max(scores, key=scores.get)
        
        # Modify the function to return the required output format.
        return {
            'anger': scores['anger'],
            'disgust': scores['disgust'],
            'fear': scores['fear'],
            'joy': scores['joy'],
            'sadness': scores['sadness'],
            'dominant_emotion': dominant_emotion
        }