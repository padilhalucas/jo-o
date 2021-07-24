def get_entity(data,entity):
    text = 'none'
    try:
        text = data.get('entities').get(entity)[0].get('body')
        print("entrou aqui")
    except:
        pass
    return text
def get_intent(data):
    try:
        data_intent = data.get('intents')
        intent = data_intent[0].get('name')
        return intent
    except:
        return 'INTENÇÃO NAO ENCONTRADA'