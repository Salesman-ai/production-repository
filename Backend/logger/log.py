import logging


class log_collection():
    backend = None
    database = None
    request = None

def setup_logger(logger_name, log_file, level=logging.INFO):
    log = logging.getLogger(logger_name)
    formatter = logging.Formatter(fmt='[%(asctime)s][%(levelname)s]: %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    log.setLevel(level)
    log.addHandler(fileHandler)
    log.addHandler(streamHandler)    

log = log_collection()

setup_logger('backend', "backend_logs.log")
setup_logger('request', "request_logs.log")
setup_logger('database', "database_logs.log")

log.backend=logging.getLogger('backend')
log.database=logging.getLogger('database')
log.request=logging.getLogger('request')