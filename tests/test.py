import unittest
import json
import sys
sys.path.append("./../")

from tasks.calculate_salaries import (separate_players_by_team, sum_scored_goals_team,
                                        assoc_levels_minimum_goals, assoc_minimum_goals_to_players,
                                        sum_team_goals_minimum)

input_calculate_salaries = json.loads(open("input_tests_calculate_salaries.json", "r").read())

class TestCalculateSalaries(unittest.TestCase):
    def test_separate_players_by_team(self):
        """
        Test that it can sum a list of integers
        """
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
        data = input_calculate_salaries['test_sum_scored_goals_team_01']

        real_result = sum_scored_goals_team( data )
        result_emulation = 19
        self.assertEqual(real_result, result_emulation)

    def test_sum_scored_goals_team_02(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        data = input_calculate_salaries['test_sum_scored_goals_team_02']

        real_result = sum_scored_goals_team( data )
        result_emulation = 37
        self.assertEqual(real_result, result_emulation)

    def test_assoc_levels_minimum_goals_01(self):
        """
        Test that it can assoc levels in dict list to a dict[level] : minimum_goals
        """
        data = input_calculate_salaries['test_assoc_levels_minimum_goals_01']

        real_result = assoc_levels_minimum_goals( data )
        result_emulation = { 
            'A' : 5,
            'B' : 10,
            'C' : 15,
            'Cuauh' : 20
         }
        self.assertEqual(real_result, result_emulation)
    
    def test_assoc_levels_minimum_goals_02(self):
        """
        Test that it can assoc levels in dict list to a dict[level] : minimum_goals
        """
        data = input_calculate_salaries['test_assoc_levels_minimum_goals_02']

        real_result = assoc_levels_minimum_goals( data )
        result_emulation = { 
            'ok':False, 'description_error': 'Unexpected name of level: None'
        }
        self.assertEqual(real_result, result_emulation)
        
    
    def test_assoc_minimum_goals_to_player_01(self):
        """
        Test that it can assoc levels in dict list to a dict[level] : minimum_goals
        """
        data = input_calculate_salaries['test_assoc_levels_minimum_goals_02']

        real_result = assoc_levels_minimum_goals( data )
        result_emulation = { 
            'ok':False, 'description_error': 'Unexpected name of level: None'
        }
        self.assertEqual(real_result, result_emulation)

    
    def test_assoc_minimum_goals_to_players_01(self):
        """
        Test that it can assoc minimum goals to a players
        """
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
                "goles_meta": 15
            },
            {  
                "nombre":"EL Cuauh",
                "nivel":"Cuauh",
                "goles":30,
                "sueldo":100000,
                "bono":30000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_meta": 20
            },
            {  
                "nombre":"Cosme Fulanito",
                "nivel":"A",
                "goles":7,
                "sueldo":20000,
                "bono":10000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_meta": 5
            },
            {  
                "nombre":"El Rulo",
                "nivel":"B",
                "goles":9,
                "sueldo":30000,
                "bono":15000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_meta": 10
            }
        ]
        self.assertEqual(real_result, result_emulation)

    def test_assoc_minimum_goals_to_players_02(self):
        """
        Test that it can assoc minimum goals to a players
        """
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
                "goles_meta": 5
            },
            {  
                "nombre":"EL Cuauh",
                "nivel":"Cuauh",
                "goles":30,
                "sueldo":100000,
                "bono":30000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_meta": 20
            },
            {  
                "nombre":"Cosme Fulanito",
                "nivel":"B",
                "goles":7,
                "sueldo":20000,
                "bono":10000,
                "sueldo_completo":None,
                "equipo":"azul",
                "goles_meta": 10
            },
            {  
                "nombre":"El Rulo",
                "nivel":"C",
                "goles":9,
                "sueldo":30000,
                "bono":15000,
                "sueldo_completo":None,
                "equipo":"rojo",
                "goles_meta": 15
            }
        ]
        self.assertEqual(real_result, result_emulation)

    def test_sum_team_goals_minimum_01(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        data = input_calculate_salaries['test_sum_team_goals_minimum_01']

        real_result = sum_team_goals_minimum( data )
        result_emulation = 25
        self.assertEqual(real_result, result_emulation)

    def test_sum_team_goals_minimum_02(self):
        """
        Test that it can sum values of dicts in a dict list
        """
        data = input_calculate_salaries['test_sum_team_goals_minimum_02']

        real_result = sum_team_goals_minimum( data )
        result_emulation = 25
        self.assertEqual(real_result, result_emulation)
        


if __name__ == '__main__':
    unittest.main()