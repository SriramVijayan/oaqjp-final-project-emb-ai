'''
This module provides functions for a server to perform emotion detection.

Functions:
1) main_page_render: To render the front-end webpage for customer interaction.
2) run_emotion_detection: To run emotion detection on received text and return results.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def main_page_render():
    '''
    Renders the front-end webpage for customer interaction.
    '''
    print("Rendering Page")
    return render_template("index.html")

@app.route("/emotionDetector")
def run_emotion_detection():
    '''
    Receives text data, runs emotion detection and returns results.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)
    if output['dominant_emotion'] is None:
        formatted_response = "<b>Invalid text! Please try again!</b>"
        return formatted_response
    formatted_response = f"For the given statement, the system response \
    is 'anger': {output['anger']}, 'disgust': {output['disgust']}, 'fear': {output['fear']}, \
    'joy': {output['joy']}, 'sadness': {output['sadness']}. \
    The dominant emotion is <b>{output['dominant_emotion']}</b>."
    return formatted_response, 200

if __name__ == "__main__":
    app.run(debug = True)
