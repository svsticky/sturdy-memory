from flask import request
from werkzeug.exceptions import BadRequest

from server.src.database.setup import db, conn
from server.src.web.utils import filter_name


def status_get():
    data = request.json

    if "name" not in data:
        raise BadRequest("Bad JSON structure")

    filtered_name = filter_name(data["name"])

    db.execute(f"SELECT * FROM current_stock WHERE name LIKE '{filtered_name}' ")

    query = db.fetchall()

    if len(query) == 0:
        raise BadRequest(f"Product {filtered_name} doesn't exist")

    return {"quantity": query[0][2]}, 200


def status_post():
    data = request.json
    filtered_name = filter_name(data["name"])

    # Enforce that the quantity is a positive integer
    if not isinstance(data["quantity"], int) or data["quantity"] < 0:
        raise BadRequest("Invalid quantity")

    db.execute(f"UPDATE current_stock SET quantity = {data["quantity"]} WHERE name LIKE '{filtered_name}';")
    conn.commit()

    return "200 OK\n"