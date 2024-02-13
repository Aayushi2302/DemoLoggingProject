
from flask import current_app as app
from flask_smorest import Blueprint
from second_log import demo_method


blp = Blueprint("name", __name__, "Name")

# logger = logging.getLogger(__name__)


@blp.route("/home")
def home_route():
    app.logger.info("Inside first_log.py Again")
    demo_method()
    return {'k': 1}