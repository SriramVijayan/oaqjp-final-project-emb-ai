from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def main_page_render():
    print("Rendering Page")
    return render_template("index.html")

@app.route("/emotionDetector")
def run_emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)
    if output['dominant_emotion'] == None:
        formatted_response = f"<b>Invalid text! Please try again!</b>"
        return formatted_response
    else:
        formatted_response = f"For the given statement, the system response \
        is 'anger': {output['anger']}, 'disgust': {output['disgust']}, 'fear': {output['fear']}, \
        'joy': {output['joy']}, 'sadness': {output['sadness']}. The dominant emotion is <b>{output['dominant_emotion']}</b>."
        return formatted_response, 200

if __name__ == "__main__":
    app.run(debug = True)