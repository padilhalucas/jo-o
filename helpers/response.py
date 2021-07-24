from wit import Wit
import os
from dotenv import load_dotenv
import json
from helpers import wit_data as wt
import random
import csv
from helpers import youtube as yt

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
    

def text_only(intent):
    answer = file_answers(intent)

def video_of():
    entity_value = wt.get_entity(witPoint.response,'subject:subject')
    video = yt.search_video("videos de " + str(entity_value))
    answer = file_answers('video_of')
    answer += "\n" + str(video)
    return answer
    

def search_video_about():
    entity_value = wt.get_entity(witPoint.response,'subject:subject')
    video = yt.search_video("videos sobre" + str(entity_value))
    answer = file_answers('video_of')
    answer += "\n" + str(video)
    return answer

def search_video_with():
    entity_value = wt.get_entity(witPoint.response,'subject:subject')
    video = yt.search_video("videos com" + str(entity_value))
    answer = file_answers('video_of')
    answer += "\n" + str(video)
    return answer

def set_volume():
    pass

def set_speed():
    pass

def set_font():
    pass

def resp(message):
    
    witPoint.response = client.message(message)
    response = witPoint.response
    print(response)
    intent = wt.get_intent(response)
    answer = dispacher(intent)
    
    return answer
    

