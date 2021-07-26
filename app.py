from flask import Flask, request
from helpers import response
app = Flask(__name__)

@app.route('/conversation', methods=['POST'])
def conversation():
    data = request.get_json()
    message = data.get('message')
    return response.resp(message)


@app.route('/init', methods=['POST'])
def init():
    response.list_intents()


if __name__ == "__main__":
    app.run()