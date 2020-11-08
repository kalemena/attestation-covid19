from flask import Flask, request, send_file
from flask_restful import Resource, Api
from json import dumps
# from flask_jsonpify import jsonify
import subprocess
import os
import time

app = Flask(__name__)
        
@app.route('/attestation', methods = ['POST'])
def attestation():
    content = request.get_json()

    template = """
    export prenom="%s"
    export nom="%s"
    export naissance_date="%s"
    export naissance_lieu="%s"
    export adresse="%s"
    # export motif_travail=""
    # export motif_courses=""
    # export motif_sante=""
    # export motif_famille=""
    # export motif_handicap=""
    # export motif_sport=""
    # export motif_judiciaire=""
    # export motif_missions=""
    # export motif_enfants=""
    export motif_%s="x"
    export fait_lieu="%s"
    export fait_date="`date +"%%d/%%m/%%Y"`"
    export fait_heures="`date +"%%H"`"
    export fait_minutes="`date +"%%M"`"
    export creation_date="`date +"%%d/%%m/%%Y"`"
    export creation_heures="`date +"%%H"`"
    export creation_minutes="`date +"%%M"`"
    """ % (
        content['prenom'],
        content['nom'],
        content['naissance_date'],
        content['naissance_lieu'],
        content['adresse'],
        content['motif'],
        content['fait_lieu']
    )

    result = subprocess.Popen("echo %s > /data/config/config.inc; make clean; make" % (template), shell=True, stdout=subprocess.PIPE).stdout.read().decode()
    try:
        return send_file('/data/attestation.pdf')
    except Exception as e:
        logging.info(e.args[0])
