import werkzeug
from time import time

from werkzeug.exceptions import BadRequest, Forbidden, NotFound, MethodNotAllowed, ImATeapot


def import_handlers(app):
    handlers = [BadRequest, Forbidden, NotFound, MethodNotAllowed, ImATeapot]

    for handler in handlers:
        app.register_error_handler(handler, handle_error)


def handle_error(e: werkzeug.exceptions.HTTPException):
    print(time(), e)
    return str(e).split(": ")[0]+"\n", int(e.code)