''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import detect_emotion

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detect():
    text_to_analyze = request.args.get('textToAnalyze')

    response = detect_emotion(text_to_analyze)

    resp = f"For the give statement, the system response is 'anger' {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['anger']}. The dominant emotion is <b>{response['dominant_emotion']}</b>."

    return resp

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
