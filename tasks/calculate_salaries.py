





def separate_players_by_team( players_json ):
    teams = {}
    for player in players_json:
        team_player = player.get('equipo')
        if team_player not in teams : teams[ team_player ] = [ player ]
        else: teams[ team_player ].append( player )
    return teams

def calculate_teams_compliance( players_json ):
    teams = separate_players_by_team( players_json )
    

    


def get_bonus_player(player):
    
    pass

def calculate_salary_for_player(player):
    fixed_salary = player.get('salario')
    bonus = get_bonus_player(player)    