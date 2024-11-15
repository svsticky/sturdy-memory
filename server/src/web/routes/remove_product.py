from flask import request
from werkzeug.exceptions import BadRequest

from server.src.database.setup import db, conn
from server.src.web.utils import filter_name


def remove_product():
    data = request.json
    # To prevent injections, only accept product names with no spaces
    filtered_name = filter_name(data["name"])

    db.execute(f"SELECT * FROM current_stock WHERE name LIKE '{filtered_name}' ")

    if len(db.fetchall()) == 0:
        raise BadRequest

    db.execute(f"DELETE FROM current_stock WHERE name LIKE '{filtered_name}' ")
    conn.commit()

    return "200 OK"