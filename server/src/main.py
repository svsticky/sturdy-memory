from flask import Flask

from server.src.web.routes.routes import import_routes
from server.src.web.exception_handlers import import_handlers
from server.src.database.setup import setup_table

if __name__ == "__main__":
    app = Flask(__name__)

    import_routes(app)
    import_handlers(app)
    setup_table()

    app.run(debug=True)