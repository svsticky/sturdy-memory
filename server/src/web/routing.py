from server.src.web.routes.product.add import *
from server.src.web.routes.product.remove import *
from server.src.web.routes.product.status import *
from server.src.web.routes.transaction import *


def import_routes(app):
    app.post("/product/add")(add)
    app.delete("/product/remove")(remove)
    app.post("/transaction")(transaction)

    app.get("/product/status")(status_get)
    app.post("/product/status")(status_post)