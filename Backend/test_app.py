
import unittest
import requests
from database.db_query import check_connection
import os
from dotenv import load_dotenv
from pathlib import Path

try:
    config_path = Path('./config.cfg')
    load_dotenv(dotenv_path=config_path)
except Exception as error:
    exit()

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
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=parameters)
        txt = result.text.replace('"','')
        self.assertEqual(result.status_code, 200)
        self.assertIsInstance(float(txt), float)

    def test_if_params_are_missing(self):
        parameters = {
            "mileage": 102200,
            "year": 2017,
            "bodyType": "minivan",
            "brand": "Toyota",
            "engineDisplacement": 1.2,
            "power": 120,
        }
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=parameters)
        self.assertEqual(result.status_code, 400)

    def test_if_year_value_are_incorrect_low(self):
        parameters = {
            "mileage": 102200,
            "year": 1888,
            "bodyType": "minivan",
            "fuelType": "Gasoline",
            "brand": "Toyota",
            "name": "Wish",
            "tranny": "CVT",
            "engineDisplacement": 1.2,
            "power": 120,
        }
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=parameters)
        self.assertEqual(result.status_code, 400)

    def test_if_year_value_are_incorrect_high(self):
        parameters = {
            "mileage": 102200,
            "year": 2024,
            "bodyType": "minivan",
            "fuelType": "Gasoline",
            "brand": "Toyota",
            "name": "Wish",
            "tranny": "CVT",
            "engineDisplacement": 1.2,
            "power": 120,
        }
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=parameters)
        self.assertEqual(result.status_code, 400)

    def test_if_engine_value_are_incorrect(self):
        parameters = {
            "mileage": 102200,
            "year": 2017,
            "bodyType": "minivan",
            "fuelType": "Gasoline",
            "brand": "Toyota",
            "name": "Wish",
            "tranny": "CVT",
            "engineDisplacement": 30,
            "power": 120,
        }
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=parameters)
        self.assertEqual(result.status_code, 400)

    def test_if_power_value_are_incorrect(self):
        parameters = {
            "mileage": 102200,
            "year": 2017,
            "bodyType": "minivan",
            "fuelType": "Gasoline",
            "brand": "Toyota",
            "name": "Wish",
            "tranny": "CVT",
            "engineDisplacement": 1.2,
            "power": 1200,
        }
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=parameters)
        self.assertEqual(result.status_code, 400)

    def test_if_params_are_not_sended(self):
        result = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict")
        self.assertEqual(result.status_code, 400)

    def test_check_database_connection(self):
        result = check_connection()
        self.assertTrue(result)

    def test_is_config_file_exists(self):
        result = os.path.isfile('./config.cfg')
        self.assertTrue(result)
    
if __name__ == '__main__':
    unittest.main()