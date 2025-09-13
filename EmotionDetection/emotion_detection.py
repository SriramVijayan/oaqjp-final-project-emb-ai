import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = json_input, headers = Headers)
    status_code = response.status_code
    if status_code == 400:
        emotions = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:    
        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score =  formatted_response['emotionPredictions'][0]['emotion']['sadness']
        score_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]
        emotion_names = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        max_score = max(score_list)
        dominant_emotion = emotion_names[score_list.index(max_score)]
        emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score,
            'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
    return emotions
