import requests

data = {'message': 'videos de comida japonesa'}
requests.post('http://127.0.0.1:5000/init')
var = requests.post('http://127.0.0.1:5000/conversation',json=data)
print(var.text)