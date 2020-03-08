import tasks.constants
from copy import copy

def get_response_correct_calculation( value : object ) -> dict:
    response = copy(tasks.constants.CORRECT_CALCULATION)
    response['description']['value'] = value
    return response

def sum_team_goals_minimum( team_players : list ) -> int:
    return sum(player['goles_meta'] for player in team_players)

def assoc_levels_minimum_goals(levels : list) -> dict:
    level_minimum = {}
    valid_levels = filter( lambda x: x if x.get('nivel') is not None else None , levels)

    for level in valid_levels:
        level_minimum[ level.get('nivel') ] = level.get('goles_minimos')

    return level_minimum

def assoc_minimum_goals_to_player(player : dict, min_goals: int) -> dict:
    player['goles_minimos'] = min_goals
    return player

def assoc_minimum_goals_to_players( players_json : dict, levels_goals : dict) -> dict:
    maping_goals_players = map( 
        lambda x: x.update( { 'goles_meta' : levels_goals.get( x.get('nivel') ) } ) or x , 
        players_json 
    )
    return list(maping_goals_players)
    

def sum_scored_goals_team( team_players : list ) -> int:
    return sum(player['goles'] for player in team_players)

def check_player_has_team( player : dict ) -> dict:
    if player.get('equipo'):
        return player

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

def add_key_value_in_dict( key : object, dict_in : dict, assign_value = None ) -> dict:
    if key not in dict_in:
        dict_in[key] = assign_value
        return dict_in
    else:
        return None

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
    if team_data.get('anotados',0) < team_data.get('meta'):
        team_compliance_dict = calculate_generic_compliance( team_data.get('anotados',0), team_data.get('meta',0) )
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
    goal = player.get('goles_meta', 0)
    compliance = 100
    if scored < goal:
        compliance = calculate_generic_compliance( scored, goal )
    if validate_dict_output_funct(compliance):
        compliance = compliance.get('description',{}).get('value',0)
    else:
        return tasks.constants.INCORRECT_CALCULATION
    return get_response_correct_calculation(compliance)
    

def get_team_compliance( player : dict ) -> float:
    

def calculate_joint_compliance( individual_compliance:float, team_compliance :float ) -> float:
    pass

def calculate_bonus_player( joint_compliance : float, complete_bonus : float ) -> float:
    pass

def get_bonus_player(player : dict) -> float:
    individual_compliance = calculate_individual_compliance( player )
    team_compliance = get_team_compliance( player )

    joint_compliance = calculate_joint_compliance( individual_compliance, team_compliance )

    final_bonus = calculate_bonus_player( joint_compliance, player.get('bono') )
    
    return final_bonus

def calculate_salary_for_player(player : dict) -> float:
    fixed_salary = player.get('salario')
    bonus = get_bonus_player(player)
    return fixed_salary + bonus