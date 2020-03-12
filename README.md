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
	 * ***Validar llaves y valores para la entrada de los jugadores (JSON)***
	 *  ***Obtener el salario completo de un jugador***: Es el proceso que obtendrá el salario completo de un jugador dado y lo colocará en el JSON de salida con la llave 'sueldo_completo'.
	 * check_keys_values_for_input_players
