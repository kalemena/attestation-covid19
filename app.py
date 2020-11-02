from flask import Flask, request, send_file
from flask_restful import Resource, Api
from json import dumps
# from flask_jsonpify import jsonify
import subprocess
import os
import time

app = Flask(__name__)
        
@app.route('/attestation')
def attestation():
    # service = request.args.get('service','')
    result = subprocess.Popen("make clean; make", shell=True, stdout=subprocess.PIPE).stdout.read().decode()
    try:
        return send_file('/data/attestation.pdf')
    except Exception as e:
        logging.info(e.args[0])
