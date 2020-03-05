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

def get_players_with_team( players_json ):
    return filter( check_player_has_team, players_json )

def separate_players_by_team( players_json : dict ) -> dict:
    teams = {}
    players_with_team = get_players_with_team( players_json )
    for player in players_with_team:
        team_player = player.get('equipo')
        if team_player not in teams : teams[ team_player ] = [ player ]
        else: teams[ team_player ].append( player )
    return teams

def calculate_teams_compliance( players_json ):
    teams = separate_players_by_team( players_json )
    compliance = {}
    for team in teams:
        compliance[team]['anotados'] = sum_scored_goals_team(teams[team])
        compliance[team]['meta'] = sum_team_goals_minimum(teams[team])
    
    return compliance


def get_bonus_player(player):
    
    pass

def calculate_salary_for_player(player):
    fixed_salary = player.get('salario')
    bonus = get_bonus_player(player)    