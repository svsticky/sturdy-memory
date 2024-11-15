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
    data = request.json

    # Check if all items exist in the database and if there's enough in stock
    for product in data["items"]:
        # Enforce that the quantity is a positive integer
        if not isinstance(product["quantity"], int) or product["quantity"] < 0:
            raise BadRequest

        filtered_name = filter_name(product["name"])

        db.execute(f"SELECT * FROM current_stock WHERE name LIKE '{filtered_name}'")
        query = db.fetchall()
        if len(query) == 0 or query[0][2] < product["quantity"]:
            raise BadRequest

    # Deduct stock
    for product in data["items"]:
        filtered_name = product["name"].split(" ")[0]
        db.execute(f"UPDATE public.current_stock SET quantity = quantity - {product["quantity"]} WHERE name LIKE '{filtered_name}';")
    conn.commit()

    return "200 OK\n"