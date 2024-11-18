from flask import request
from werkzeug.exceptions import BadRequest

from server.src.database.setup import db, conn
from server.src.web.utils import filter_name


# {
#   "items": [
#     {
#       "name": "waffles",
#       "quantity": 21
#     }
#   ]
# }
def transaction():
    data: dict = request.json

    if "items" not in data:
        raise BadRequest("Bad JSON structure")

    # Check if all items exist in the database and if there's enough in stock
    for product in data["items"]:
        if "name" not in product or "quantity" not in product:
            raise BadRequest("Bad JSON structure")


        # Enforce that the quantity is a positive integer
        if not isinstance(product["quantity"], int) or product["quantity"] < 0:
            raise BadRequest("Invalid quantity")

        filtered_name = filter_name(product["name"])

        db.execute(f"SELECT * FROM current_stock WHERE name LIKE '{filtered_name}'")
        query = db.fetchall()
        if len(query) == 0:
            raise BadRequest(f"Product {filtered_name} not found")
        if query[0][2] < product["quantity"]:
            raise BadRequest(f"Not enough stock for {filtered_name}")

    # Deduct stock
    for product in data["items"]:
        filtered_name = product["name"].split(" ")[0]
        db.execute(f"UPDATE current_stock SET quantity = quantity - {product["quantity"]} WHERE name LIKE '{filtered_name}';")
    conn.commit()

    return "200 OK\n"
