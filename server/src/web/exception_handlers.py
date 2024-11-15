import werkzeug

from werkzeug.exceptions import BadRequest, Forbidden, NotFound, MethodNotAllowed, ImATeapot


def import_handlers(app):
    handlers = [BadRequest, Forbidden, NotFound, MethodNotAllowed, ImATeapot]

    for handler in handlers:
        app.register_error_handler(handler, handle_error)


def handle_error(e: werkzeug.exceptions.HTTPException):
    return f"{e.code} {str(e.description)}\n", e.code
