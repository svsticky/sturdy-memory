from server.src.routes.add_product import add_product

def import_routes(app):
    app.post("/add-product")(add_product)