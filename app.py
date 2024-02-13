import logging
from flask import Flask, g, request
from flask.logging import default_handler
import shortuuid
from first_log import blp as HomeBlp
from api_setup import config_app
from log_config import CustomFormatter
from flask.logging import create_logger

def create_app():
    app = Flask(__name__)
    config_app()
    app.register_blueprint(HomeBlp)

    @app.before_request
    def generate_request_id():
        g.request_id = shortuuid.ShortUUID().random(length=5)

    # with app.app_context():
    # logger = logging.getLogger('werkzeug')
    # app.logger.removeHandler(default_handler)
    formatter = CustomFormatter(fmt='%(asctime)s - %(levelname)-10s - [%(request_id)s] - %(message)s')
    handler = logging.FileHandler("logs.log")
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    return app
