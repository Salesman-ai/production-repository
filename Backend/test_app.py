
import unittest
import requests
from database.db_query import check_connection
import os

class RunTest(unittest.TestCase):

    def test_connect_with_prediction(self):
        parameters = {
            "mileage": 102200,
            "year": 2017,
            "bodyType": "minivan",
            "fuelType": "Gasoline",
            "brand": "Toyota",
            "name": "Wish",
            "tranny": "CVT",
            "engineDisplacement": 1.2,
            "power": 120,
        }
        result = requests.get("http://172.20.0.11:8090/api-prediction/get-predict", params=parameters)
        self.assertTrue(result)
        self.assertIsInstance(float(result.text), float)

    def test_check_database_connection(self):
        result = check_connection()
        self.assertTrue(result)

    def test_is_config_file_exists(self):
        result = os.path.isfile('./config.cfg')
        self.assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()