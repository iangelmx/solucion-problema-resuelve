import unittest
import json
import sys
sys.path.append("./../")

import tasks.constants
from tasks.calculate_salaries import (separate_players_by_team, sum_scored_goals_team,
                                        assoc_levels_minimum_goals, assoc_minimum_goals_to_players,
                                        sum_team_goals_minimum, check_player_has_team, get_players_with_team,
                                        assoc_goal_and_scored_goals_per_team, calculate_teams_compliance,
                                        calculate_generic_compliance, calculate_joint_compliance,
                                        calculate_bonus_player, get_bonus_player, calculate_salary_for_player,
                                        calculate_individual_compliance, get_desired_types_constant,
                                        check_desired_input_types, validate_value_key,
                                        verify_process_output
                                        )

input_calculate_salaries = json.loads(open("input_tests_calculate_salaries.json", "r").read())

class TestCalculateSalaries(unittest.TestCase):
    def test_separate_players_by_team(self):
        """
        Test that it can sum a list of integers
        """
        print("test_separate_players_by_team")
        data = input_calculate_salaries['test_01']
        real_result = separate_players_by_team(data)

        result_emulation = {
                'rojo' : [ 
                    {  
                        "nombre":"Juan Perez",
                        "nivel":"C",
                        "goles":10,
                        "sueldo":50000,
                        "bono":25000,
                        "sueldo_completo":None,
                        "equipo":"rojo"
                    },
                        {  
                        "nombre":"El Rulo",
                        "nivel":"B",
                        "goles":9,
                        "sueldo":30000,
                        "bono":15000,
                        "sueldo_completo":None,
                        "equipo":"rojo"
                    } 
                ],
                'azul':[
                    {  
                        "nombre":"EL Cuauh",
                        "nivel":"Cuauh",
                        "goles":30,
                        "sueldo":100000,
                        "bono":30000,
                        "sueldo_completo":None,
                        "equipo":"azul"
                    },
                    {  
                        "nombre":"Cosme Fulanito",
                        "nivel":"A",
                        "goles":7,
                        "sueldo":20000,
                        "bono":10000,
                        "sueldo_completo":None,
                        "equipo":"azul"
                    },
                ]
        }
        self.assertEqual(real_result, result_emulation)

    def test_sum_scored_goals_team_01(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        print("test_sum_scored_goals_team_01")
        data = input_calculate_salaries['test_sum_scored_goals_team_01']

        real_result = sum_scored_goals_team( data )
        result_emulation = 19
        self.assertEqual(real_result, result_emulation)

    def test_sum_scored_goals_team_02(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        print("test_sum_scored_goals_team_02")
        data = input_calculate_salaries['test_sum_scored_goals_team_02']

        real_result = sum_scored_goals_team( data )
        result_emulation = 37
        self.assertEqual(real_result, result_emulation)

    def test_assoc_levels_minimum_goals_01(self):
        """
        Test that it can assoc levels in dict list to a dict[level] : minimum_goals
        """
        print("test_assoc_levels_minimum_goals_01")
        data = input_calculate_salaries['test_assoc_levels_minimum_goals_01']

        real_result = assoc_levels_minimum_goals( data )
        result_emulation = (True, 200, { 
            'A' : 5,
            'B' : 10,
            'C' : 15,
            'Cuauh' : 20
        })
        self.assertEqual(real_result, result_emulation)
    
    def test_assoc_levels_minimum_goals_02(self):
        """
        Test that it can assoc levels in dict list to a dict[level] : minimum_goals
        """
        print("test_assoc_levels_minimum_goals_02")
        data = input_calculate_salaries['test_assoc_levels_minimum_goals_02']

        real_result = assoc_levels_minimum_goals( data )
        result_emulation = (True, 200, { 
            'A' : 5,
            'B' : 10,
            'C' : 15
        })
        self.assertEqual(real_result, result_emulation)
    
    def test_assoc_levels_minimum_goals_03(self):
        """
        Test that it can assoc levels in dict list to a dict[level] : minimum_goals
        """
        print("test_assoc_levels_minimum_goals_03")
        data = "Some different to dict/JSON"

        real_result = assoc_levels_minimum_goals( data )
        result_emulation = (False, 400, { 
        })
        self.assertEqual(real_result, result_emulation)

    
    def test_assoc_minimum_goals_to_players_01(self):
        """
        Test that it can assoc minimum goals to a players
        """
        print("test_assoc_minimum_goals_to_players_01")
        jugadores = input_calculate_salaries['test_assoc_minimum_goals_to_players_01']['jugadores']
        niveles = input_calculate_salaries['test_assoc_minimum_goals_to_players_01']['niveles_goles_assoc']

        real_result = assoc_minimum_goals_to_players( jugadores, niveles )
        result_emulation = [  
            {  
                "nombre":"Juan Perez",
                "nivel":"C",
                "goles":10,
                "sueldo":50000,
                "bono":25000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_minimos": 15
            },
            {  
                "nombre":"EL Cuauh",
                "nivel":"Cuauh",
                "goles":30,
                "sueldo":100000,
                "bono":30000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_minimos": 20
            },
            {  
                "nombre":"Cosme Fulanito",
                "nivel":"A",
                "goles":7,
                "sueldo":20000,
                "bono":10000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_minimos": 5
            },
            {  
                "nombre":"El Rulo",
                "nivel":"B",
                "goles":9,
                "sueldo":30000,
                "bono":15000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_minimos": 10
            }
        ]
        self.assertEqual(real_result, result_emulation)

    def test_assoc_minimum_goals_to_players_02(self):
        """
        Test that it can assoc minimum goals to a players
        """
        print("test_assoc_minimum_goals_to_players_02")
        jugadores = input_calculate_salaries['test_assoc_minimum_goals_to_players_02']['jugadores']
        niveles = input_calculate_salaries['test_assoc_minimum_goals_to_players_01']['niveles_goles_assoc']

        real_result = assoc_minimum_goals_to_players( jugadores, niveles )
        result_emulation = [  
            {  
                "nombre":"Juan Perez",
                "nivel":"A",
                "goles":10,
                "sueldo":50000,
                "bono":25000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_minimos": 5
            },
            {  
                "nombre":"EL Cuauh",
                "nivel":"Cuauh",
                "goles":30,
                "sueldo":100000,
                "bono":30000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_minimos": 20
            },
            {  
                "nombre":"Cosme Fulanito",
                "nivel":"B",
                "goles":7,
                "sueldo":20000,
                "bono":10000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_minimos": 10
            },
            {  
                "nombre":"El Rulo",
                "nivel":"C",
                "goles":9,
                "sueldo":30000,
                "bono":15000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_minimos": 15
            }
        ]
        self.assertEqual(real_result, result_emulation)

    def test_sum_team_goals_minimum_01(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        print("test_sum_team_goals_minimum_01")
        data = input_calculate_salaries['test_sum_team_goals_minimum_01']

        real_result = sum_team_goals_minimum( data )
        result_emulation = 25
        self.assertEqual(real_result, result_emulation)

    def test_sum_team_goals_minimum_02(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        print("test_sum_team_goals_minimum_02")
        data = input_calculate_salaries['test_sum_team_goals_minimum_02']

        real_result = sum_team_goals_minimum( data )
        result_emulation = 25
        self.assertEqual(real_result, result_emulation)

    
    def test_check_player_has_team_01(self):
        """
        Test that it can filter and return only the players with a team or with a valid name of team
        """
        print("test_check_player_has_team_01")
        data = input_calculate_salaries['test_check_player_has_team_01']['jugador']

        real_result = check_player_has_team( data )
        result_emulation = {  
            "nombre":"EL Cuauh",
            "nivel":"Cuauh",
            "goles":30,
            "sueldo":100000,
            "bono":30000,
            "sueldo_completo":None,
            "equipo":"azul",
            "goles_minimos" : 20 
        }
        self.assertEqual(real_result, result_emulation)

    def test_check_player_has_team_02(self):
        """
        Test that it can filter and return only the players with a team or with a valid name of team
        """
        print("test_check_player_has_team_02")
        data = input_calculate_salaries['test_check_player_has_team_02']['jugador']

        real_result = check_player_has_team( data )
        result_emulation = None
        self.assertEqual(real_result, result_emulation)

    def test_check_player_has_team_03(self):
        """
        Test that it can filter and return only the players with a team or with a valid name of team
        """
        print("test_check_player_has_team_03")
        data = input_calculate_salaries['test_check_player_has_team_03']['jugador']

        real_result = check_player_has_team( data )
        result_emulation = None
        self.assertEqual(real_result, result_emulation)

    def test_get_players_with_team_01(self):
        """
        Test that it can filter and return only the players with a team or with a valid name of team
        """
        print("test_get_players_with_team_01")
        data = input_calculate_salaries['test_get_players_with_team_01']

        real_result = get_players_with_team( data )
        result_emulation = [
            {  
                "nombre":"Cosme Fulanito",
                "nivel":"A",
                "goles":7,
                "sueldo":20000,
                "bono":10000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_minimos" : 5
            },
            {  
                "nombre":"El Rulo",
                "nivel":"B",
                "goles":9,
                "sueldo":30000,
                "bono":15000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_minimos" : 10
            } 
        ]
        parsing_result = list(real_result)
        self.assertEqual( parsing_result, result_emulation )

    
    def test_assoc_team_goal_and_scored_goals_01(self):
        """
        Test that it can assoc the goal and the scored goals 
        for each team of a list of players
        """
        print("test_assoc_team_goal_and_scored_goals_01")

        data = input_calculate_salaries['test_assoc_minimum_goals_to_players_02']['jugadores']

        real_result = assoc_goal_and_scored_goals_per_team( data )
        result_emulation = {
            'rojo' : {
                'anotados': 19,
                'meta': 20
            },
            'azul': {
                'anotados' : 37,
                'meta' : 30
            }
        }
        
        self.assertEqual( real_result, result_emulation )
    
    def test_assoc_team_goal_and_scored_goals_02(self):
        """
        Test that it can assoc the goal and the scored goals 
        for each team of a list of players
        """
        print("test_assoc_team_goal_and_scored_goals_02")

        data = input_calculate_salaries['test_assoc_team_goal_and_scored_goals_02']['jugadores']

        real_result = assoc_goal_and_scored_goals_per_team( data )
        result_emulation = {
            'verde':{
                'anotados': 10,
                'meta': 5
            },
            'rojo' : {
                'anotados': 9,
                'meta': 15
            },
            'azul': {
                'anotados' : 37,
                'meta' : 30
            }
        }
        
        self.assertEqual( real_result, result_emulation )

    def test_calculate_generic_compliance_01(self):
        """
        Test that it can calculate de generic compliance according a goal and scored goals
        when scored is equals or greater than goal
        """
        print("test_calculate_generic_compliance_01")
        data = input_calculate_salaries['test_calculate_generic_compliance']['test_01']

        real_result = calculate_generic_compliance( data['scored_goals'], data['goal_goals'] )
        result_emulation = {
            'ok':True, 
            'status_code':200, 
            'description':{
                'value': 100
            }
        }
        self.assertEqual( real_result, result_emulation )

    def test_calculate_generic_compliance_02(self):
        """
        Test that it can calculate de generic compliance according a goal and scored goals
        when scored is smaller than goal
        """
        print("test_calculate_generic_compliance_02")
        data = input_calculate_salaries['test_calculate_generic_compliance']['test_02']

        real_result = calculate_generic_compliance( data['scored_goals'], data['goal_goals'] )
        result_emulation = {
            'ok':True, 
            'status_code':200, 
            'description':{
                'value': 50
            }
        }
        self.assertEqual( real_result, result_emulation )
    def test_calculate_generic_compliance_03(self):
        """
        Test that it fails to calculate de generic compliance according a goal and scored goals
        when goal is zero
        """
        print("test_calculate_generic_compliance_03")
        data = input_calculate_salaries['test_calculate_generic_compliance']['test_03']

        real_result = calculate_generic_compliance( data['scored_goals'], data['goal_goals'] )
        result_emulation = {
            'ok':False, 
            'status_code':500, 
            'description':"Zero value provided for goal."
        }
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_teams_compliance_01(self):
        """
        Test that it can assoc the goal and the scored goals 
        for each team of a list of players
        """
        print("test_calculate_teams_compliance_01")
        data = input_calculate_salaries['test_assoc_minimum_goals_to_players_02']['jugadores']

        real_result = calculate_teams_compliance( data )
        result_emulation = {
            'rojo' : (19*100/20),
            'azul': 100
        }
        
        self.assertEqual( real_result, result_emulation )

    
    def test_calculate_teams_compliance_02(self):
        """
        Test that it can assoc the goal and the scored goals 
        for each team of a list of players
        """
        print("test_calculate_teams_compliance_02")

        data = input_calculate_salaries['test_assoc_team_goal_and_scored_goals_02']['jugadores']

        real_result = calculate_teams_compliance( data )
        result_emulation = {
            'verde' : 100,
            'rojo' : (9*100/15),
            'azul': 100
        }
        
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_joint_compliance_01(self):
        """
        Test that it calculate the joint compliance like an average of 2 compliances, 
        the team compliance and individual compliance
        """
        print("test_calculate_joint_compliance_01")
        data = input_calculate_salaries['test_calculate_joint_compliance']['test_01']

        real_result = calculate_joint_compliance( data['individual_compliance'], data['team_compliance'] )
        result_emulation = 97.5
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_joint_compliance_02(self):
        """
        Test that it calculate the joint compliance like an average of 2 compliances, 
        the team compliance and individual compliance
        """
        print("test_calculate_joint_compliance_02")
        data = input_calculate_salaries['test_calculate_joint_compliance']['test_02']

        real_result = calculate_joint_compliance( data['individual_compliance'], data['team_compliance'] )
        result_emulation = 90.5
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_joint_compliance_03(self):
        """
        Test that it calculate the joint compliance like an average of 2 compliances, 
        the team compliance and individual compliance
        """
        print("test_calculate_joint_compliance_03")

        data = input_calculate_salaries['test_calculate_joint_compliance']['test_03']

        real_result = calculate_joint_compliance( data['individual_compliance'], data['team_compliance'] )
        result_emulation = 83.9445
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_bonus_player_01(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_calculate_bonus_player_01")

        data = input_calculate_salaries['test_calculate_bonus_player']['test_01']

        real_result = calculate_bonus_player( data['joint_compliance'], data['bonus'] )
        result_emulation = 50000
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_bonus_player_02(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_calculate_bonus_player_02")
        data = input_calculate_salaries['test_calculate_bonus_player']['test_02']

        real_result = calculate_bonus_player( data['joint_compliance'], data['bonus'] )
        result_emulation = 24375
        self.assertEqual( real_result, result_emulation )
    
    def test_calculate_bonus_player_03(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """

        print("test_calculate_bonus_player_03")

        data = input_calculate_salaries['test_calculate_bonus_player']['test_03']

        real_result = calculate_bonus_player( data['joint_compliance'], data['bonus'] )
        result_emulation = 11546.415
        self.assertEqual( real_result, result_emulation )
    
    def test_get_bonus_player_01(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """

        print("test_get_bonus_player_01")

        data = input_calculate_salaries['test_get_bonus_player']['test_01']
        real_result = get_bonus_player( data['player'], data['teams_compliance'] )
        #i_c = (10*100/15)
        #t_c = ( 95 )
        #j_c = ((10*100/15) + 95)/2
        #f_b = 25000 * (((10*100/15) + 95)/2)/100
        result_emulation = 25000 * (((10*100/15) + 95)/2)/100
        self.assertEqual( real_result, result_emulation )
    
    def test_get_bonus_player_02(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_get_bonus_player_02")

        data = input_calculate_salaries['test_get_bonus_player']['test_02']
        real_result = get_bonus_player( data['player'], data['teams_compliance'] )
        #i_c = 100
        #t_c = ( 68.59 )
        #j_c = 84.295
        #f_b = 30000 * ( 84.295 )/100
        result_emulation = 30000 * ( 84.295 )/100
        self.assertEqual( real_result, result_emulation )
    
    def test_get_bonus_player_03(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_get_bonus_player_03")

        data = input_calculate_salaries['test_get_bonus_player']['test_03']
        real_result = get_bonus_player( data['player'], data['teams_compliance'] )
        #i_c = 80
        #t_c = 0
        #j_c = 40
        #f_b = 500 * ( 40 )/100
        result_emulation = 200
        self.assertEqual( real_result, result_emulation )

    def test_calculate_salary_for_player_01(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_calculate_salary_for_player_01")

        data = input_calculate_salaries['test_get_bonus_player']['test_01']
        real_result = calculate_salary_for_player( data['player'], data['teams_compliance'] )
        #i_c = (10*100/15)
        #t_c = ( 95 )
        #j_c = ((10*100/15) + 95)/2
        #f_b = 25000 * (((10*100/15) + 95)/2)/100
        #s = 50000
        result_emulation = (25000 * (((10*100/15) + 95)/2)/100) + 50000
        self.assertEqual( real_result, result_emulation )

    def test_calculate_salary_for_player_02(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_calculate_salary_for_player_02")

        data = input_calculate_salaries['test_get_bonus_player']['test_02']
        real_result = calculate_salary_for_player( data['player'], data['teams_compliance'] )
        #i_c = 100
        #t_c = ( 68.59 )
        #j_c = 84.295
        #f_b = 30000 * ( 84.295 )/100
        #s = 100000
        result_emulation = 125288.5
        self.assertEqual( real_result, result_emulation )

    def test_calculate_salary_for_player_03(self):
        """
        Test that it calculate the final bonus of a player according the joint compliance
        and the bonus
        """
        print("test_calculate_salary_for_player_03")
        data = input_calculate_salaries['test_get_bonus_player']['test_03']
        real_result = calculate_salary_for_player( data['player'], data['teams_compliance'] )
        #i_c = 80
        #t_c = 0
        #j_c = 40
        #f_b = 500 * ( 40 )/100
        #s = 2600
        result_emulation = 2800
        self.assertEqual( real_result, result_emulation )

    def test_calculate_individual_compliance_01(self):
        """
        Test that it calculate the individual compliance of a player according his level, scored
        goals and goal goals.
        """
        print("test_calculate_individual_compliance_01")
        data = input_calculate_salaries['test_calculate_individual_compliance']['test_01']
        real_result = calculate_individual_compliance( data )

        result_emulation = {
            'ok':True, 
            'status_code':200, 
            'description':{
                'value':(12*100)/15
            }
        }
        self.assertEqual( real_result, result_emulation )

    def test_calculate_individual_compliance_02(self):
        """
        Test that it calculate the individual compliance of a player according his level, scored
        goals and goal goals.
        """
        print("test_calculate_individual_compliance_02")
        data = input_calculate_salaries['test_calculate_individual_compliance']['test_02']
        real_result = calculate_individual_compliance( data )

        result_emulation = {
            'ok':True, 
            'status_code':200, 
            'description':{
                'value' : 0,
            }
        }
        self.assertEqual( real_result, result_emulation )

    def test_calculate_individual_compliance_03(self):
        """
        Test that it calculate the individual compliance of a player according his level, scored
        goals and goal goals.
        """
        print("test_calculate_individual_compliance_03")
        data = input_calculate_salaries['test_calculate_individual_compliance']['test_03']
        real_result = calculate_individual_compliance( data )

        result_emulation = {
            'ok':True, 
            'status_code':200, 
            'description':{
                'value' : 100,
            }
        }
        self.assertEqual( real_result, result_emulation )

    def test_get_desired_types_constant_01(self):
        """
        Test that it cant retrieve the correct constant for function
        """
        print("test_get_desired_types_constant_01")
        data = input_calculate_salaries['test_get_desired_types_constant']['test_01']
        real_result = get_desired_types_constant( data )

        result_emulation = {
            'goles' : [int],
            'nivel' : [str],
            'equipo' : [str, int],
            'bono' : [int, float],
            'sueldo' : [int, float],
            'nombre' : [str]
        }
        self.assertEqual( real_result, result_emulation )

    def test_get_desired_types_constant_02(self):
        """
        Test that it cant retrieve the correct constant for function
        """
        print("test_get_desired_types_constant_02")
        data = input_calculate_salaries['test_get_desired_types_constant']['test_02']
        real_result = get_desired_types_constant( data )

        result_emulation = {
            'goles_minimos' : [int],
            'nivel' : [str, int],
        }
        self.assertEqual( real_result, result_emulation )
    
    def test_get_desired_types_constant_03(self):
        """
        Test that it cant retrieve the correct constant for function
        """
        print("test_get_desired_types_constant_03")
        data = input_calculate_salaries['test_get_desired_types_constant']['test_03']
        real_result = get_desired_types_constant( data )

        result_emulation = {}
        self.assertEqual( real_result, result_emulation )

    def test_check_desired_input_types_01(self):
        """
        Test that it can check if input types are correct according the 
        kind of input and the input dict
        """
        print("test_check_desired_input_types_01")
        data = input_calculate_salaries['test_check_desired_input_types']['test_01']
        real_result = check_desired_input_types( data['key'], data['dictionary'], data['kind_input'] )

        result_emulation = True
        self.assertEqual( real_result, result_emulation )

    def test_check_desired_input_types_02(self):
        """
        Test that it can check if input types are correct according the 
        kind of input and the input dict
        """
        print("test_check_desired_input_types_02")
        data = input_calculate_salaries['test_check_desired_input_types']['test_02']
        real_result = check_desired_input_types( data['key'], data['dictionary'], data['kind_input'] )

        result_emulation = False
        self.assertEqual( real_result, result_emulation )

    def test_check_desired_input_types_03(self):
        """
        Test that it can check if input types are correct according the 
        kind of input and the input dict
        """
        print("test_check_desired_input_types_03")
        data = input_calculate_salaries['test_check_desired_input_types']['test_03']
        real_result = check_desired_input_types( data['key'], data['dictionary'], data['kind_input'] )

        result_emulation = False
        self.assertEqual( real_result, result_emulation )

    def test_check_desired_input_types_04(self):
        """
        Test that it can check if input types are correct according the 
        kind of input and the input dict
        """
        print("test_check_desired_input_types_04")
        data = input_calculate_salaries['test_check_desired_input_types']['test_04']
        real_result = check_desired_input_types( data['key'], data['dictionary'], data['kind_input'] )

        result_emulation = True
        self.assertEqual( real_result, result_emulation )
    
    def test_validate_value_key_01(self):
        """
        Test that it can verify if key in dict and its value it not None
        """
        print("test_validate_value_key_01")
        data = input_calculate_salaries['test_validate_value_key']['test_01']
        real_result = validate_value_key( data['key'], data['player'] )

        result_emulation = None
        self.assertEqual( real_result, result_emulation )

    def test_validate_value_key_02(self):
        """
        Test that it can verify if key in dict and its value it not None
        """
        print("test_validate_value_key_02")
        data = input_calculate_salaries['test_validate_value_key']['test_02']
        real_result = validate_value_key( data['key'], data['player'] )

        result_emulation = data['key']
        self.assertEqual( real_result, result_emulation )


    def test_verify_process_output_01(self):
        """
        Test that it can verify if de output of a process is valid according his lenght
        """
        print("test_verify_process_output_01")
        data = input_calculate_salaries['test_verify_process_output']['test_01']
        real_result = verify_process_output( data )

        result_emulation = (True, 200)
        self.assertEqual( real_result, result_emulation )

    def test_verify_process_output_02(self):
        """
        Test that it can verify if de output of a process is valid according his lenght
        """
        print("test_verify_process_output_02")
        data = input_calculate_salaries['test_verify_process_output']['test_02']
        real_result = verify_process_output( data )

        result_emulation = (True, 200)
        self.assertEqual( real_result, result_emulation )

    def test_verify_process_output_03(self):
        """
        Test that it can verify if de output of a process is valid according his lenght
        """
        print("test_verify_process_output_03")
        data = input_calculate_salaries['test_verify_process_output']['test_03']
        real_result = verify_process_output( data )

        result_emulation = (False, 400)
        self.assertEqual( real_result, result_emulation )

    def test_verify_process_output_04(self):
        """
        Test that it can verify if de output of a process is valid according his lenght
        """
        print("test_verify_process_output_04")
        data = input_calculate_salaries['test_verify_process_output']['test_04']
        real_result = verify_process_output( data )

        result_emulation = (False, 500)
        self.assertEqual( real_result, result_emulation )
    


        
        


if __name__ == '__main__':
    unittest.main()