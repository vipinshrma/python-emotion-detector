"""
This module provides a function to detect emotions in text using the IBM Watson NLU API.
"""
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def emotion_detector(text_to_analyze):
    """
    Analyzes the provided text and returns a dictionary of emotion scores.
    """
    base_url = os.getenv("URL")
    url = f"{base_url}/v1/analyze?version=2019-07-12"
    key = os.getenv("API_KEY")

    payload = {
        "text": text_to_analyze,
        "features": {"emotion": {}}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers, auth=('apikey', key))

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotion']['document']['emotion']

    # Extracting scores and finding dominant emotion
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    result['dominant_emotion'] = max(result, key=result.get)

    return result