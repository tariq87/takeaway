import socket

from flask import Flask
from flask import request
from flask import jsonify

from mq_helper import producer

app = Flask(__name__)

@app.route('/')
def docker():
    return "Hey, we have flask app running in a docker container - {}!".format(socket.gethostname())

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    producer(message)
    return jsonify(message), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
