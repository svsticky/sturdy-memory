from flask import request

from server.src.database.setup import db, conn

def remove_product():
    response = request.json

    db.execute(f"SELECT * FROM current_stock WHERE name like '{response["name"]}' ")

    if len(db.fetchall()) == 0:
        return '{"status": "400", "msg": "Product with that name does not exist."}', 400

    db.execute(f"DELETE FROM current_stock WHERE name like '{response["name"]}' ")
    conn.commit()

    return "200 OK"