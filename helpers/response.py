from wit import Wit
import os
from dotenv import load_dotenv
import json
from helpers import wit_data as wt
import random
import csv
from helpers import youtube as yt
import requests

class witClass:
    response = {}

load_dotenv()

WIT_TOKEN = os.getenv("WIT_TOKEN")
client = Wit(WIT_TOKEN)

op = {}
witPoint = witClass()

def file_answers(intent):
    data = ''
    with open("Json-Answ", "r") as file:
        data = json.loads(file.read())

    answer = data.get(intent)[random.randint(0,2)].get("text")
    return answer

def list_intents():
    intents_com = []
    with open('intent_list.csv','r') as fl:
        reader = csv.reader(fl)
        for linha in reader:
            try:
              mount_comands(linha)
            except:
              print(linha)

def mount_comands(comands):
    op[comands[0]]=eval(comands[1])


def dispacher(intent):
    return str(op[intent]())
    

def text_only():
    intent = wt.get_intent(witPoint.response)
    answer = file_answers(intent)
    return answer

def video_of():
    entity_value = wt.get_entity_value(witPoint.response,'subject:subject')
    video = yt.search_video("videos de " + str(entity_value))
    answer = file_answers('video_of')
    answer += "@@@" + str(video)
    return answer
    
def personalized_answer(intent, values):
    answer = file_answers(intent)
    answer


def about_me():
    name = wt.get_entity_value(witPoint.response,'name:name')
    location = wt.get_entity_value(witPoint.response,'wit$location:location')
    age = location = wt.get_entity_value(witPoint.response,'wit$duration:duration') #sometimes NLP doesn't take age with age_of_person
    if age is None:
        age = location = wt.get_entity_value(witPoint.response,'wit$age_of_person:age_of_person')
    
    #aqui vamos usar a resposta personalizada, falta implementar
    answer = file_answers('about_me')
    return answer

def introduce_bot():
    answer = file_answers('introduce_bot')
    return answer

def video_about():
    entity_value = wt.get_entity_value(witPoint.response,'subject:subject')
    video = yt.search_video("videos sobre" + str(entity_value))
    answer = file_answers('video_of')
    answer += "@@@" + str(video)
    return answer

def movie_recsys():
    entity_value = wt.get_entity_value(witPoint.response,'movie:movie')
    try:
        req = requests.get('https://recsys-joao.herokuapp.com/movie?title=' + str(entity_value))
    
        part = req.json()
        movie = part[0].get('Name')
        video = yt.search_video("trailer oficial " + str(movie))
        answer = file_answers('movie_recsys')
        answer += "@@@" + str(video)
        return answer
    except:
        return 'Infelizmente não consegui encontrar seu vídeo, mas você pode perguntar por outro se quiser.'

def video_with():
    entity_value = wt.get_entity_value(witPoint.response,'subject:subject')
    video = yt.search_video("videos com" + str(entity_value))
    answer = file_answers('video_of')
    answer += "@@@" + str(video)
    return answer

def set_volume():
    pass

def set_speed():
    pass

def set_font():
    pass

def dataTreatment(answer):
    data = {}
    dataSliced = answer.split("@@@")
    if len(dataSliced) ==1:
        data['msg'] = str(dataSliced[0])
    else:
        print(dataSliced)
        data['msg'] = str(dataSliced[0])
        data['video'] = str(dataSliced[1])
    return data
    
    
def resp(message):
    
    witPoint.response = client.message(message)
    response = witPoint.response
    print(response)
    intent = wt.get_intent(response)
    answer = dispacher(intent)
    data = dataTreatment(answer)
    

    return data
    

