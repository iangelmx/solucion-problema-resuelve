import tasks.constants
from copy import copy

'''Generic functions'''

def remove_dict_keys( keys_to_remove:list , dictionary : dict ) -> dict:
    new_dict = { key : value for (key, value) in dictionary.items() if key not in keys_to_remove }
    return new_dict

def add_key_value_in_dict( key : object, dict_in : dict, assign_value = None ) -> dict:
    new_dict = copy(dict_in)
    if key not in new_dict:
        new_dict[key] = assign_value
        return new_dict
    else:
        return None

def return_fatal_error_to_client( response_funct ):
    if isinstance(response_funct, dict) and response_funct.get('ok') == False:
        return response_funct
    else:
        return False

''' Functions to map, filter or reduce '''

def check_level_goal( level ):
    if level.get('nivel') and level.get('goles_minimos'):
        return level

def check_player_has_team( player : dict ) -> dict:
    if player.get('equipo'):
        return player


'''Kind of helpers'''

def get_response_correct_calculation( value : object ) -> dict:
    response = copy(tasks.constants.CORRECT_CALCULATION)
    response['description']['value'] = value
    return response

def sum_team_goals_minimum( team_players : list ) -> int:
    try:
        return sum(player['goles_minimos'] for player in team_players)
    except Exception:
        return {'ok':False, 'status_code': 404,'description':'There is not indicated "goles_minimos" for at least 1 team'}



def assoc_levels_minimum_goals(levels : list) -> dict:
    level_minimum = {}
    valid_levels = filter( check_level_goal , levels)

    for level in valid_levels:
        level_minimum[ level.get('nivel') ] = level.get('goles_minimos')

    return level_minimum

def assoc_minimum_goals_to_player(player : dict, min_goals: int) -> dict:
    player_copy = copy(player)
    player_copy['goles_minimos'] = min_goals
    return player_copy

def assoc_minimum_goals_to_players( players_json : dict, levels_goals : dict) -> dict:
    maping_goals_players = map( 
        lambda x: x.update( { 'goles_minimos' : levels_goals.get( x.get('nivel') ) } ) or x , 
        players_json 
    )
    return list(maping_goals_players)
    

def sum_scored_goals_team( team_players : list ) -> int:
    try:
        return sum(player['goles'] for player in team_players)
    except KeyError:
        return {'ok':False, 'status_code': 404,'description':'There is not indicated "goles" for at least 1 player'}

def get_players_with_team( players_json : dict ) -> filter:
    return filter( check_player_has_team, players_json )

def separate_players_by_team( players_json : dict ) -> dict:
    teams = {}
    players_with_team = get_players_with_team( players_json )
    for player in players_with_team:
        team_player = player.get('equipo')
        if team_player not in teams : teams[ team_player ] = [ player ]
        else: teams[ team_player ].append( player )
    return teams


def assoc_goal_and_scored_goals_per_team( players_json : dict ) -> dict:
    teams = separate_players_by_team( players_json )
    goal_and_scored_goals_teams = {}
    for team in teams:
        goal_and_scored_goals_teams = add_key_value_in_dict(team, goal_and_scored_goals_teams, {})
        goal_and_scored_goals_teams[team]['anotados'] = sum_scored_goals_team(teams[team])
        goal_and_scored_goals_teams[team]['meta'] = sum_team_goals_minimum(teams[team])
    return goal_and_scored_goals_teams

def validate_dict_output_funct( response_funct : object ) -> bool:
    if response_funct.get('ok') == True:
        return True
    else:
        print(f"Status error: {response_funct.get('status_code')}. Details: {response_funct.get('description')}")
        return False

def calculate_generic_compliance( scored : int, goal : int ) -> dict:
    try:
        compliance = scored * 100 / goal
        return get_response_correct_calculation(compliance)
    except ZeroDivisionError:
        return tasks.constants.INCORRECT_CALCULATION

def calculate_compliance_of_team( team_data : dict ) -> dict:
    team_compliance_val = 100
    scored = team_data.get('anotados',0)
    goal = team_data.get('meta',0)
    if scored < team_data.get('meta'):
        team_compliance_dict = calculate_generic_compliance( scored , goal )
        if validate_dict_output_funct(team_compliance_dict):
            team_compliance_val = team_compliance_dict.get('description',{}).get('value',0)
        else:
            return tasks.constants.INCORRECT_CALCULATION
    return get_response_correct_calculation(team_compliance_val)

def calculate_teams_compliance( players_json : dict ) -> dict:
    teams_goal_and_scored_goals = assoc_goal_and_scored_goals_per_team( players_json )
    compliances = {}
    for team in teams_goal_and_scored_goals:
        compliance_team = calculate_compliance_of_team( teams_goal_and_scored_goals[team] )
        if validate_dict_output_funct( compliance_team ):
            compliances[team] = compliance_team.get('description').get('value')
    return compliances

def calculate_individual_compliance( player : dict ) -> dict:
    scored = player.get('goles', 0)
    goal = player.get('goles_minimos', 0)
    compliance = 100
    if scored < goal:
        compliance = calculate_generic_compliance( scored, goal )
        if validate_dict_output_funct(compliance):
            compliance = compliance.get('description',{}).get('value',0)
        else:
            return tasks.constants.INCORRECT_CALCULATION
    return get_response_correct_calculation(compliance)
    
def get_team_compliance( player : dict, compliances:dict ) -> float:
    team_player = player.get('equipo')
    return compliances.get( team_player, 0 )

def calculate_joint_compliance( individual_compliance:float, team_compliance :float ) -> float:
    return (individual_compliance + team_compliance) / 2

def calculate_bonus_player( joint_compliance : float, complete_bonus : float ) -> float:
    return complete_bonus * ( joint_compliance / 100 )

def get_bonus_player(player : dict, teams_compliance:dict) -> float:
    individual_compliance = calculate_individual_compliance( player ).get('description', {}).get('value',0)
    team_compliance = get_team_compliance( player, teams_compliance )

    joint_compliance = calculate_joint_compliance( individual_compliance, team_compliance )

    final_bonus = calculate_bonus_player( joint_compliance, player.get('bono') )
    return final_bonus

def calculate_salary_for_player(player : dict, teams_compliance : dict) -> float:
    fixed_salary = player.get('sueldo',0)
    bonus = get_bonus_player(player, teams_compliance)
    return sum([fixed_salary, bonus])

def get_complete_salary_for_player(player : dict, teams_compliance : dict)->dict:
    new_player = copy(player)
    new_player['sueldo_completo'] = calculate_salary_for_player( player, teams_compliance )
    new_player = remove_dict_keys(['nivel'], new_player)
    return new_player