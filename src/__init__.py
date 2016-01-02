import os
import sys
import logging


def get_debug():
    try:
        return bool(int(os.environ.get('DEBUG', False)))
    except ValueError:
        return False

DEBUG = get_debug()

root_logger = logging.getLogger('')
root_logger.setLevel(logging.INFO)

formatter = logging.Formatter('[%(name)s/%(levelname)s]: %(message)s')
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

file_formatter = logging.Formatter('[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s')
file_handler = logging.FileHandler('logs/camw.log', mode='a+')
file_handler.setFormatter(file_formatter)

root_logger.addHandler(stream_handler)
root_logger.addHandler(file_handler)
