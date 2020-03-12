# Resolución Problema Ingeniería Resuelve

En este archivo README se explica a mejor detalle la solución generada al problema de ingeniería de Resuelve (disponible en: [https://github.com/resuelve/prueba-ing-backend](https://github.com/resuelve/prueba-ing-backend))

# Descripción del problema:
De forma sintetizada, se necesita generar una solución o programa que pueda recibir a la entrada un JSON con la estructura siguiente:

    [
	  {
	    "nombre":"Juan Perez",
	    "nivel":"C",
        "goles":10,
        "sueldo":50000,
        "bono":25000,
        "sueldo_completo":null,
        "equipo":"rojo"
	  },
	  ...,
	  {
	    "nombre":"EL Cuauh",
	    "nivel":"Cuauh",
        "goles":30,
        "sueldo":100000,
        "bono":30000,
        "sueldo_completo":null,
        "equipo":"azul"
	  }
	]
    
De acuerdo al nivel de cada jugador, deberá anotar un número de goles, el cual dependiendo de su cumplimiento decidirá si se le paga de forma completa o parcial su bono.
Para mayor detalle, tablas de niveles y ejemplo de casos, se puede consultar de forma completa el problema en:
[https://github.com/resuelve/prueba-ing-backend#problema](https://github.com/resuelve/prueba-ing-backend#problema)


# Análisis y diseño

## Requisitos funcionales:

- Calcular el sueldo completo de cada jugador contemplando el sueldo fijo y el variable con el *bono calculado*
- Llenar en el JSON de salida la llave ``sueldo_completo`` del JSON de entrada con la siguiente estructura:
`[

{

"nombre":"El Rulo",

"goles_minimos":10,

"goles":9,

"sueldo":30000,

"bono":15000,

"sueldo_completo": 14250,

"equipo":"rojo"

}

]`

## Requerimientos no funcionales:

- Calcular el alcance individual de cada jugador de acuerdo a la cantidad de goles anotados contra la meta que debió cubrir.
- Calcular el alcance por equipo de los jugadores de acuerdo a la cantidad de goles anotados en conjunto contra los que se debían anotar.
- Calcular el bono que se le deberá pagar a cada jugador con base en el alcance individual y el de su equipo.

## Diseño general de la solución

La solución funcionará bajo una aplicación web con diseño estructurado, semi-funcional puesto que no requiere de mayor complejidad el cálculo del sueldo completo de cada jugador de Resuelve FC.

### Endpoints identificados
  
1.  **/resuelve/calculate-salaries**: Es el endpoint que tomará el JSON de entrada de los jugadores y calculará el sueldo para cada uno de ellos. Responderá con el JSON completo.
	* Sólo soporta peticiones **POST**
2.  **/resuelve/receive-levels**: Es el endpoint que recibirá el JSON con los niveles y goles mínimos y actualizará los niveles actuales para poder calcular el sueldo completo de otro club o del mismo Resuelve FC.
3. **/resuelve/reset-levels**: Este endpoint reestablecerá a los niveles y goles mínimos predeterminados del Resuelve FC.
4. **/** : Es el endpoint de la raíz de la aplicación, la cual despliega una página web que busca brindar documentación de cómo consumir los endpoints.

### Módulos necesarios para el correcto funcionamiento de los endpoints

 1.  **/resuelve/calculate-salaries**: 
	 * ***Validar llaves y valores para la entrada de los jugadores***: Es el proceso que revisa que la entrada tenga los parámetros necesarios y tengan valores válidos para poder calcular el salarios de los jugadores. Si algún jugador no cumple con los tipos de dato o con los parámetros, detiene el proceso y lo informa. Las funciones involucradas en este proceso son:
		 * check_required_keys
			 * validate_value_key
			 * check_desired_input_types
	 *  ***Asociar goles  mínimos a los jugadores***: Este proceso da una pasada a los jugadores recibidos y les asigna los goles mínimos que debieron anotar de acuerdo a su nivel.
	 * ***Calcular el alcance de los equipos***: Es el proceso que, con base en los goles anotados y niveles de los jugadores, calcula el alcance de cada equipo y lo devuelve al resto del flujo. Las funciones involucradas en este proceso son:
		 * assoc_goal_and_scored_goals_per_team
			 * separate_players_by_team
			 * add_key_value_in_dict
			 * sum_scored_goals_team
			 * sum_team_goals_minimum
		 * calculate_compliance_of_team
			 * calculate_generic_compliance
			 * validate_dict_output_funct
			 * get_response_correct_calculation

	 *  ***Obtener el salario completo de los jugadores***: Es el proceso que obtendrá el salario completo de los jugadores y lo colocará en el JSON de salida con la llave 'sueldo_completo'. Las funciones involucradas en este proceso son:
		 * calculate_salary_for_player
			 * get_bonus_player
				 * calculate_individual_compliance
				 * get_team_compliance
				 * calculate_joint_compliance
				 * calculate_bonus_player
			 * remove_dict_keys
	 * ***Verificar salida del proceso*** : Evalúa los resultados de obtener el salario de todos los jugadores y prepara la respuesta del endpoint.

2.  **/resuelve/receive-levels**:
	* ***Validar llaves y valores para la entrada de los jugadores***: Es el proceso que revisa que la entrada tenga los parámetros necesarios y tengan valores válidos para poder calcular el salarios de los jugadores. Si algún jugador no cumple con los tipos de dato o con los parámetros, detiene el proceso y lo informa.
	* ***Asociar niveles y goles mínimos***: Es el proceso que actualiza los niveles y goles mínimos del club para los jugadores y los guarda en una estructura de datos que pueden consultar los demás endpoints.
		* check_level_goal

3.  **/resuelve/reset-levels**: 
	* ***Asociar niveles y goles mínimos***: Es el proceso que actualiza los niveles y goles mínimos predeterminados para los jugadores y los guarda en una estructura de datos que pueden consultar los demás endpoints.
		* check_level_goal

  

### Descripción del flujo de datos en los endpoints/funciones:


|Entrada|Módulo|Salida|
|----------------|------------|----------------|
|*-JSON con los datos de los jugadores* : ***JSON*** | `/resuelve/calculate-salaries` | - JSON con el sueldo_completo calculado de los jugadores : ***JSON*** -JSON con los errores identificados al momento de evaluar la entrada : ***JSON*** -JSON con los errores identificados al momento de calcular el sueldo de los jugadores : ***JSON*** |
| *-Lista de llaves necesarias para cálculo de sueldo* : ***list*** *-JSON con los datos de los jugadores* : ***JSON***| `check_keys_values_for_input()` | Lista de llaves faltantes o que tienen valores no válidos para calculo de sueldo de jugador : ***list*** |
| *-JSON con los datos de los jugadores* : ***dict***. | `assoc_minimum_goals_to_players()` | JSON de los jugadores con la llave 'goles_minimos' añadida : ***dict*** |
|*-JSON con los datos de los jugadores* : ***dict***| `calculate_teams_compliance()` | Diccionario con los alcances indicados por equipo : ***dict***|
|*-Datos de un jugador dado* : ***dict*** *-Alcance por equipos* : ***dict***| `get_complete_salary_for_player()` | Diccionario del jugador con la llave y valor de 'sueldo_completo' calculado : ***dict***|
|*-Lista o diccionario de salida de un proceso* : ***dict***| `verify_process_output()` | Tupla con estatus de realización : ***tuple***|
|*-Lista de diccionarios con los niveles y goles mínimos del club* : ***list***| `assoc_levels_minimum_goals()` | Diccionario de niveles y goles mínimos : ***dict***|

  

# Arquitectura
- La solución corre sobre Python en su versión 3.7.3 de 64 bits con el framework Flask en su versión 1.0.2.
- Se recomienda que corra bajo un entorno virtual debido a que se requieren librerías fuera del estándar.
- El proyecto está organizado de acuerdo al framework de Flask
```
solucion-prueba-resuelve
.
| -- tasks
	|-- calculate_salaries.py
	|-- constants.py
| -- templates
	| -- error_pages
		| -- 40X.html
		| -- 50X.html
	| -- base.html
	| -- main.html
| -- tests
	 | -- test.py
	 | -- input_tests_calculate_salaries.json
|-- Procfile
|-- runtime.txt
|-- requirements.txt
|-- settings.json
|-- app.py (Web app flask)
|-- LICENSE
|-- README.md
``` 
## Librerías necesarias
1.  **json** (librería estándar del lenguaje Python)
2.  **unittest** (librería estándar del lenguaje Python)
3.  **copy**  (librería estándar del lenguaje Python)
4.  **gunicorn**
5.  **flask**
6.  **itsdangerous**
7.  **Jinja2** 
8.  **Click**
9.  **Werkzeug**
10.  **MarkupSafe** 

## Forma de probarlo
La forma más sencilla de probar la solución es mediante un cliente para hacer peticiones web como Postman o Insomnia.

La URL en donde se pueden probar los endpoints es: 
[https://ws-solucion-problema-resuelve.herokuapp.com/](https://ws-solucion-problema-resuelve.herokuapp.com/) añadiendo al final la ruta de los endpoints que se quiera probar.

Para el cálculo de los salarios del Resuelve FC:
**Sólo tolera peticiones POST**
[https://ws-solucion-problema-resuelve.herokuapp.com/resuelve/calculate-salaries](https://ws-solucion-problema-resuelve.herokuapp.com/resuelve/calculate-salaries)
Ejemplo de JSON de entrada:
```
[  
   {  
      "nombre":"Juan Perez",
      "nivel":"C",
      "goles":10,
      "sueldo":50000,
      "bono":25000,
      "sueldo_completo":null,
      "equipo":"rojo"
   },
   {  
      "nombre":"EL Cuauh",
      "nivel":"Cuauh",
      "goles":30,
      "sueldo":100000,
      "bono":30000,
      "sueldo_completo":null,
      "equipo":"azul"
   }
]
```

Para actualizar los niveles y goles mínimos:
**Sólo tolera peticiones POST**
[https://ws-solucion-problema-resuelve.herokuapp.com/resuelve/receive-levels](https://ws-solucion-problema-resuelve.herokuapp.com/resuelve/receive-levels)

Para reestablecer a los niveles predeterminados del Resuelve FC:
**Sólo tolera peticiones GET**
[https://ws-solucion-problema-resuelve.herokuapp.com/resuelve/reset-levels](https://ws-solucion-problema-resuelve.herokuapp.com/resuelve/reset-levels)