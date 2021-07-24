import requests

data = {'message': 'Oi, tudo bem?'}

var = requests.post('http://127.0.0.1:5000/conversation',json=data)
print(var.text)