from flask import Flask

from server.src.routes.routes import import_routes
from server.src.exception_handlers import import_handlers

if __name__ == "__main__":
    app = Flask(__name__)

    import_routes(app)
    import_handlers(app)

    app.run(debug=True)