"""
Module to analyse emotions
"""
import json
import requests

"""
Function to analyse the emotion of the text given as parameter
"""
def detect_emotion(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=headers, timeout=40)
    
    dic = json.loads(response.text)['emotionPredictions'][0]['emotion']
    
    val = 0
    em = ''
    for key in dic:
        if val <= dic[key]:
            em = key
            val = dic[key]
    dic['dominant_emotion'] = em
    return dic

    

