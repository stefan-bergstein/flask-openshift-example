import os
import logging
import socket
from flask import Flask, jsonify

HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'flask')
IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))
HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())
ENV_NAME = os.environ.get('ENV_NAME', 'test')

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'env_name': ENV_NAME,
        'host_name': HOST_NAME,
        'app_name': APP_NAME,
        'ip': IP,
        'port': PORT,
        'home_dir': HOME_DIR,
        'host': socket.gethostname()
    })

@app.route('test')
def iot():
    return jsonify({
        'vibration': '0.2',
        'temperature': '84.2'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
