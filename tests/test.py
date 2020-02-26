import unittest
import json
import sys
sys.path.append("./../")

from tasks.calculate_salaries import separate_players_by_team

input_calculate_salaries = json.loads(open("input_tests_calculate_salaries.json", "r").read())

class TestCalculateSalaries(unittest.TestCase):
    def test_separate_players_by_team(self):
        """
        Test that it can sum a list of integers
        """
        data = input_calculate_salaries['test_01']
        result = separate_players_by_team(data)

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
        self.assertEqual(result, result_emulation)

if __name__ == '__main__':
    unittest.main()