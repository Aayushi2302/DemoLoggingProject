import logging

from flask import current_app
from log_config import CustomFormatter
# from logtail import LogtailHandler
from flask.logging import create_logger

request_id = "app12345"

# def logging_configuration():
#     my_formatter = logging.Formatter("%(asctime)s [%(request_id)s] : %(message)s")
#     # my_cloud_handler = LogtailHandler(source_token = "NrM64d57ZmUzAa8Ayq9RbiK9")
#     my_handler = logging.FileHandler("logs.log")
#     my_handler.setFormatter(my_formatter)
#     # my_cloud_handler.setFormatter(my_formatter)
#     my_handler.addFilter(CustomFilter(request_id))
#     # my_cloud_handler.addFilter(CustomFilter())
#     root_logger = logging.getLogger()
#     root_logger.setLevel(logging.DEBUG)
#     root_logger.addHandler(my_handler)
#     # root_logger.addHandler(my_cloud_handler)

def logging_configuration():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    my_formatter = CustomFormatter(fmt="%(asctime)s [%(request_id)s] : %(message)s")
    my_handler = logging.FileHandler("logs.log")
    my_handler.setFormatter(my_formatter)
    logger.addHandler(my_handler)

def config_app():
    # logging_configuration()
    pass