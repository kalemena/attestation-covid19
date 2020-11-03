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
    export motif_travail="%s"
    export motif_courses="%s"
    export motif_sante="%s"
    export motif_famille="%s"
    export motif_handicap="%s"
    export motif_sport="%s"
    export motif_judiciaire="%s"
    export motif_missions="%s"
    export motif_enfants="%s"
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
        content['motif_travail'],
        content['motif_courses'],
        content['motif_sante'],
        content['motif_famille'],
        content['motif_handicap'],
        content['motif_sport'],
        content['motif_judiciaire'],
        content['motif_missions'],
        content['motif_enfants'],
        content['fait_lieu']
    )

    result = subprocess.Popen("echo %s > /data/config/config.inc; make clean; make" % (template), shell=True, stdout=subprocess.PIPE).stdout.read().decode()
    try:
        return send_file('/data/attestation.pdf')
    except Exception as e:
        logging.info(e.args[0])
