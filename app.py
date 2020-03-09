# -----------------------------------------------------------
# Prueba técnica backend, Resuelve
#
# (C) 2020 Angel Negib Ramirez Alvarez, CDMX, Mexico
# Released under GNU Public License (GPL)
# email iangelmx.isc@gmail.com 
# Este script calcula el salario completo del Resuelve FC
# con base en un JSON de entrada. El problema a resolver se
# encuentra disponible en:
# https://github.com/resuelve/prueba-ing-backend
# El presente fue construido con Python en su versión 3.7.3 
# Está diseñado para la puesta en producción en sistemas 
# que soporten el paradigma de la programación estructurada.
# La documentación completa de la solución está disponible en
# el archivo README del repositorio:
# https://github.com/iangelmx/solucion-problema-resuelve
# -----------------------------------------------------------


# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, redirect, render_template
import tasks.calculate_salaries
from tasks.calculate_salaries import *
import json

env = json.loads( open("settings.json", "r").read() )
FLASK_PREFIX_APP = env['prefix_api']

app = Flask(__name__)
current_levels = assoc_levels_minimum_goals( env['metas_predeterminadas'] )

'''ERROR HANDLERS'''
@app.errorhandler(404)
def not_found(error):
	return render_template('./error_pages/40X.html', number_err=404, label_err="Not Found", text_error="El recurso que estás solicitando no existe."),404

@app.errorhandler(405)
def method_not_allowed(error):
	return render_template('./error_pages/40X.html', number_err=405, label_err="Method Not Allowed", text_error="La ruta estipulada no tolera el método solicitado."),405

@app.errorhandler(410)
def file_gone(error):
    return render_template('./error_pages/40X.html', number_err=405, label_err="Gone", text_error="Gone, the file you search now have gone."),410

@app.errorhandler(500)
def intServErr(error):
	return render_template('./error_pages/50X.html',errorInfo=error),500


@app.route("/")
def pred_route():
    return render_template("main.html")

@app.route(FLASK_PREFIX_APP+"/receive-levels", methods=["POST"])
def receive_levels():
    global current_levels
    new_levels = request.json
    current_levels = assoc_levels_minimum_goals( new_levels )
    return jsonify(ok=True, status_code=200, description={'levels_received':current_levels})

@app.route(FLASK_PREFIX_APP+"/calculate-salaries", methods=["POST"])
def receive_players():
    input_data = request.json

    players = assoc_minimum_goals_to_players( input_data, current_levels )
    
    teams_compliance = calculate_teams_compliance(input_data)

    players = [ get_complete_salary_for_player(x, teams_compliance) for x in players ]
    
    return jsonify(ok=True, status_code = 200, description={'players_salary':players})

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=443)