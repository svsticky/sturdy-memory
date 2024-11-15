from flask import request
from werkzeug.exceptions import BadRequest

from server.src.database.setup import db, conn
from server.src.web.utils import filter_name


def add_product():
    data = request.json
    filtered_name = filter_name(data["name"])

    db.execute(f"SELECT * FROM current_stock WHERE name LIKE '{filtered_name}' ")

    if len(db.fetchall()) != 0:
        raise BadRequest

    db.execute(f"INSERT INTO current_stock (name, quantity) VALUES ('{filtered_name}', 0)")
    conn.commit()

    return "200 OK"