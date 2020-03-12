CORRECT_CALCULATION ={
    'ok':True, 
    'status_code':200, 
    'description':{
        'value':0
    }
}

INCORRECT_CALCULATION ={
    'ok':False, 
    'status_code':500, 
    'description':"Zero value provided for goal."
}

INCORRECT_CALCULATION_NONE_VALUE ={
    'ok':False, 
    'status_code':500, 
    'description':{
        'details_error' : "There aren't values for this calculation.",
    }
}

NECESARY_KEYS_PLAYER = [
    "goles", "nivel", "equipo", "bono", "sueldo", "nombre"
]

DESIRED_DATA_TYPES = {
    'goles' : [int],
    'nivel' : [str],
    'equipo' : [str],
    'bono' : [int, float],
    'sueldo' : [int, float],
    'nombre' : [str]
}

NECESARY_KEYS_LEVELS = [
    "goles_minimos", "nivel"
]