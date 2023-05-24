from flask import Flask, request, make_response, json
import os
from dotenv import load_dotenv
from pathlib import Path
from logger.log import log
from database.db_query import insert_price
from database.db_initialize import is_database_exist
from flask_cors import CORS
import requests
import time


app = Flask(__name__)
cors = CORS(app, resources={r"/api-backend/*": {"origins": "*"}})

time.sleep(15)
log.backend.info("Start working on the logic module...")
is_database_exist()

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


@app.route('/api-backend/get-price', methods=['POST'])
def get_price():
    if request.method == 'POST':
        req = request.get_json()
        res = None
        log.backend.info(f"Function 'get_price()' started")
        log.request.info(f"Request was received from <{request.remote_addr}>.")


        try:
            for key in req:
                if req[key] == '':
                    log.request.error(f"Request received from failed. Missing parameters.")
                    return summary("Missing parameters", 400)
        except Exception as e:
            log.request.error(f"Request received from failed. Missing parameters.")
            return summary("Missing parameters", 400)
        
        if req["year"] < 1900:
            log.request.error(f"Request received from failed. Year parameter is too low.")
            return summary("Year parameter is too low", 400)
        
        if req["year"] > 2023:
            log.request.error(f"Request received from failed. Year parameter is too high.")
            return summary("Year parameter is too high", 400)

        if req["power"] > 1000:
            log.request.error(f"Request received from failed. Power parameter is too high.")
            return summary("Power parameter is too high", 400)
        
        if req["engineDisplacement"] > 20:
            log.request.error(f"Request received from failed. Engine parameter is too high.")
            return summary("Engine parameter is too high", 400)

        try:
            log.request.info(f"Request was sent to the prediction module")
            try:
                res = requests.get(os.environ.get("PREDICTION_URL") +  ":" + os.environ.get("PREDICTION_PORT") + "/api-prediction/get-predict", params=req)
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
        
        insert_price(req["brand"], req["name"], req["bodyType"], req["fuelType"], req["tranny"], req["power"], req["mileage"],req["year"],req["engineDisplacement"], float(res.text))
        res = summary(float(res.text), 200)
        log.request.info(f"Response returned")
        log.backend.info(f"Function 'get_price()' finished")
        return res


if __name__ == '__main__':
    app.run(debug=True, port=8080)
