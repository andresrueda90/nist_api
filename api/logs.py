import logging
import os
from datetime import datetime


class LogsConfig:
    DEFAULT_HISTORY = "static/logs/history.log"

    def __init__(self):
        super().__init__()

    @staticmethod
    def config():
        log_file = LogsConfig.create_log_file()
        if log_file:
            logging.basicConfig(filename=log_file, level=logging.INFO,
                                format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    @staticmethod
    def create_log_file() -> str:
        try:
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")
            log_file = f'static/logs/{year}/{month}/history_{year}_{month}_{day}.log'
            log_directory = os.path.dirname(log_file)
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)
            return log_file
        except Exception as e:
            return LogsConfig.DEFAULT_HISTORY
