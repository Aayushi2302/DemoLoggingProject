from flask import current_app as app

# logger = logging.getLogger(__name__)

def demo_method():
    app.logger.critical("Inside second log")