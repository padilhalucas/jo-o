from wit import Wit
import os
from dotenv import load_dotenv
import json
import wit_data as wt
import random
import csv


load_dotenv()

WIT_TOKEN = os.getenv("WIT_TOKEN")
client = Wit(WIT_TOKEN)

op = {}
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
    op[comands[0]]=comands[1]


def dispacher(intent):
    return op[intent]
    

def text_only(intent):
    answer = file_answers(intent)

def search_video_of():
    pass

def search_video_about():
    pass

def search_video_with():
    pass

def set_volume():
    pass

def set_speed():
    pass

def set_font():
    pass

def resp(message):
    response = client.message(message)
    intent = wt.get_intent(response)
    answer = dispacher(intent)
    
    return response
    

