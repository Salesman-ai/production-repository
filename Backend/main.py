from flask import Flask, request, make_response, json
import os
from dotenv import load_dotenv
from pathlib import Path
from logger.log import log
from database.db_query import insert_price
from database.db_initialize import is_database_exist


app = Flask(__name__)
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


@app.route('/api/get-price')
def get_price():
    #prediction = None
    response = None
    #code = None
    log.backend.info(f"Function 'get_price()' started")
    log.request.info(f"Request was received from <{request.remote_addr}>.")
    try:
        request_data = request.args
        log.request.info(f"Request was sent to the prediction module")
        try:
            #prediction = requests.get(url = os.getenv('PREDICTION_URL'), params = request_data)
            #prediction = request_data['kurwa']
            log.request.info(f"Response was received from  prediction module")
        
        except Exception as error:
            log.request.error(f"Response was not obtained from the prediction model. Error log - {error}")
    
    except Exception as error:
        log.backend.error(f"Function 'get_price()' failed. Status: {error}")
        log.request.error(f"Request received from <{request.remote_addr}> failed.")
    finally:
        #response = summary(10000, 200)
        #insert_price(1, str(request.remote_addr), "honda", "civic", 10000)
        log.request.info(f"Response returned")
        log.backend.info(f"Function 'get_price()' finished")
        return response


if __name__ == '__main__':
    log.backend.info("Start working on the logic module...")
    is_database_exist()
    app.run(debug=True, port=8080)
