from flask import Flask, request, make_response, json
import os
from dotenv import load_dotenv
from pathlib import Path
from logger.log import log
from database.db_query import insert_price
from database.db_initialize import is_database_exist
from flask_cors import CORS
import requests


app = Flask(__name__)
cors = CORS(app, resources={r"/api-backend/*": {"origins": "*"}})

try:
    config_path = Path('./config.cfg')
    load_dotenv(dotenv_path=config_path)
except Exception as error:
    log.backend.error(f"Failed to load configuration file - {error}")
    exit()


def summary(body, status_code):
    return app.response_class(response=json.dumps(body),
                              status=status_code,
                              mimetype='application/json')


frontend_fixers = {
    "mileage": float,
    "year": float,
    "bodyType": str,
    "fuelType": str,
    "brand": str,
    "name": str,
    "tranny": str,
    "engineDisplacement": float,
    "power": float,
}

@app.route('/api-backend/get-price', methods=['GET'])
def get_price():
    if request.method == 'GET':
        req = request.form.to_dict()
        log.request.info(f"Request <{req}>.")
        res = None
        log.backend.info(f"Function 'get_price()' started")
        log.request.info(f"Request was received from <{request.remote_addr}>.")

        try:
            log.request.info(f"Request was sent to the prediction module")
            try:
                res = requests.get("http://172.20.0.11:8090/api-prediction/get-predict", params=req)
                log.request.info(f"Response was received from  prediction module")
            
            except Exception as error:
                log.request.error(f"Response was not obtained from the prediction model. Error log - {error}")
                res = summary("Connection to prediction server failure...", 503)
                return res
        
        except Exception as error:
            log.backend.error(f"Function 'get_price()' failed. Status: {error}")
            log.request.error(f"Request received from <{request.remote_addr}> failed.")
            res = summary("Connection failure...", 500)
            return res
        
        res = summary(float(res.text), 200)
        log.request.info(f"Response returned")
        log.backend.info(f"Function 'get_price()' finished")
        return res


if __name__ == '__main__':
    log.backend.info("Start working on the logic module...")
    #is_database_exist()
    app.run(debug=True, port=8080)
