from server.src.web.routes.add_product import add_product
from server.src.web.routes.remove_product import remove_product

def import_routes(app):
    app.post("/add-product")(add_product)
    app.post("/remove-product")(remove_product)