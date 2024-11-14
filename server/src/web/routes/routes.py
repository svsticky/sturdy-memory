from server.src.web.routes.add_product import add_product

def import_routes(app):
    app.post("/add-product")(add_product)