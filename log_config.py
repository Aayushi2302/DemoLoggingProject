import logging
from flask import g

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(g, 'request_id'):
            record.request_id = g.request_id
        else:
            record.request_id = 'N/A'
        return super().format(record)
