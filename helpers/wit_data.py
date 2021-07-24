def get_entity(data):
    try:
        pass
    except:
        pass

def get_intent(data):
    try:
        data_intent = data.get('intents')
        intent = data_intent[0].get('name')
        return intent
    except:
        return 'INTENÇÃO NAO ENCONTRADA'