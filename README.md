# Emotion Detection Pipeline

This is a Flask-based web application that uses the IBM Watson Natural Language Understanding (NLU) API to detect emotions in text.

## Features
- Analyzes text for 5 emotions: Anger, Disgust, Fear, Joy, and Sadness.
- Identifies the dominant emotion.
- Robust error handling for invalid or empty input.
- Unit tests included for core logic verification.

## Installation
1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your Watson `API_KEY` and `URL`.

## Usage
Run the server:
```bash
python3 server.py
```
Visit `http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy` to see the results.
