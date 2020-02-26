# -----------------------------------------------------------
# Prueba técnica backend, Resuelve
#
# (C) 2020 Angel Negib Ramirez Alvarez, CDMX, Mexico
# Released under GNU Public License (GPL)
# email iangelmx.isc@gmail.com {
# Este script calcula el salario completo del Resuelve FC
# con base en un JSON de entrada. El problema a resolver se
# encuentra disponible en:
# https://github.com/resuelve/prueba-ing-backend
# El presente fue construido con Python en su versión 3.7.3 
# Está diseñado para la puesta en producción en sistemas 
# que soporten el paradigma de la programación estructurada.
# La documentación completa de la solución está disponible en
# el archivo README del repositorio:
# https://github.com/iangelmx/solucion-prueba-resuelve
# -----------------------------------------------------------


# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS, cross_origin
import tasks.calculate_salaries
import json

env = json.loads( open("settings.json", "r").read() )
FLASK_PREFIX_APP = env['prefix_api']

app = Flask(__name__)

@app.route(FLASK_PREFIX_APP+"/receive-levels", methods=["POST"])
def receive_levels():
    input_data = request.json

@app.route(FLASK_PREFIX_APP+"/calculate-salaries", methods=["POST"])
def receive_players():
    input_data = request.json

    compliance_teams = calculate_teams_compliance(input_data)

    for jugador in input_data:
        jugador = tasks.calculate_salaries._calculate_salary_for_player(jugador)
    
    return jsonify(ok=True, description=input_data)

    

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)