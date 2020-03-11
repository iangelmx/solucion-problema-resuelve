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

########################################################################################
######################
### ERROR HANDLERS ###
######################
@app.errorhandler(400)
def bad_request(error):
    return jsonify(ok=False, status_code=400, description_error="You've done a bad request, check your input")

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

########################################################################################

@app.route("/")
def pred_route() -> flask.template_rendered:
    """Cuando se hace una petición a la raíz de la aplicación
     Se retorna el template con una pequeña explicación de como
     se puede invocar a los demás endpoints."""

    return render_template("main.html")

@app.route(FLASK_PREFIX_APP+"/reset-levels", methods=["GET"])
def receive_levels() -> dict:
    """
    Este endpoint pretende reiniciar a los valores iniciales 
    de los niveles y goles mínimos del Resuelve FC.
    
        Sólo tolera peticiones POST.
        Retorna un JSON especificando si se logró realizar la actualización
        de los niveles. En la descripción retorna los niveles predeterminados actualizados.
    """
    current_levels = assoc_levels_minimum_goals( env['metas_predeterminadas'] )

    return jsonify(ok=current_levels[0], status_code=current_levels[1], description={'saved_levels':current_levels[3]} )


@app.route(FLASK_PREFIX_APP+"/receive-levels", methods=["POST"])
def receive_levels():
    """
    Este endpoint recibe los niveles y goles mínimos asociados
    a otros clubes, para que puedan calcular el bono de sus jugadores.
        Sólo tolera peticiones POST
        Recibe a la entrada un arreglo de JSON's del tipo:
        [
            { "nivel" : "A", "goles_minimos" : 5 },
            { "nivel" : "B", "goles_minimos" : 10} 
        ]
        Retorna un JSON especificando si se logró realizar la actualización
        y en la descripción retorna los niveles que se lograron guardar como:
        { 
            ok:false, 
            status_code:400, 
            description: { 
                'saved_levels':[] 
            } 
        }
    """
    global current_levels
    new_levels = request.json
    current_levels = assoc_levels_minimum_goals( new_levels )
    return jsonify(ok=current_levels[0], status_code=current_levels[1], description={'saved_levels':current_levels[3]} )

@app.route(FLASK_PREFIX_APP+"/calculate-salaries", methods=["POST"])
def receive_players():
    """
    El presente endpoint calcula el sueldo completo de los jugadores del
    Resuelve FC y de otros clubes de acuerdo a su sueldo, bono y alcance conjunto de cada
    jugador.
        Sólo soporta peticiones POST
        Recibe una arreglo de JSON's como:
        [  
            {  
                "nombre":"Juan Perez",
                "nivel":"C",
                "goles":10,
                "sueldo":50000,
                "bono":25000,
                "sueldo_completo":null,
                "equipo":"rojo"
            }
        ]

        Retorna un JSON con el estatus de si se pudo realizar alguna evaluación
        y con el sueldo completo calculado, como el siguiente:
        {
            ok:true,
            status_code:200
        }
        [  
            {  
                "nombre":"Juan Perez",
                "goles_minimos":15,
                "goles":10,
                "sueldo":50000,
                "bono":25000,
                "sueldo_completo":66666.66666666667,
                "equipo":"rojo"
            }, ...
        ]
        
    """
    input_data = request.json
    players = assoc_minimum_goals_to_players( input_data, current_levels )
    teams_compliance = calculate_teams_compliance(input_data)
    players = [ get_complete_salary_for_player(x, teams_compliance) for x in players ]

    status_task = verify_process_output( players )
    
    return jsonify(ok=status_task[0], status_code = status_task[1], description={'players_salary':players})

    

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=443)