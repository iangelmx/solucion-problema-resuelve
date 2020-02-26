def assoc_levels_minimum_goals(levels : list) -> dict:
    level_minimum = {}
    for level in levels:
        level_name = level.get('nivel')
        if level_name is not None: level_minimum[ level_name ] = level.get('goles_minimos')
        else: return {'ok':False, 'description_error': f"Unexpected name of level: {level_name}"}
    return level_minimum

def assoc_minimum_goals_to_player(player : dict, min_goals: int) -> dict:
    player['goles_minimos'] = min_goals
    return player

def sum_scored_goals_team( team_players : list ) -> int:
    return sum(player['goles'] for player in team_players)

def separate_players_by_team( players_json ):
    teams = {}
    for player in players_json:
        team_player = player.get('equipo')
        if team_player and team_player not in teams : teams[ team_player ] = [ player ]
        else: teams[ team_player ].append( player )
    return teams

def calculate_teams_compliance( players_json ):
    teams = separate_players_by_team( players_json )
    compliance = {}
    for team in teams:
        print("Team a evaluar:", team, ":>",teams[team])
        teams[team]['anotados'] = sum_scored_goals_team(teams[team])
        
        #teams[team]['meta'] = sum_goal_team( teams[team] )




    # Necesito: {
    #  * Puntos alcanzados  por jugador
    #  * Puntos meta        por jugador
    #  }
    #
    #

    


def get_bonus_player(player):
    
    pass

def calculate_salary_for_player(player):
    fixed_salary = player.get('salario')
    bonus = get_bonus_player(player)    