from flask import request

from server.src.database.setup import db, conn

def add_product():

    response = request.json

    db.execute(f"SELECT * FROM current_stock WHERE name like '{response["name"]}' ")

    if len(db.fetchall()) != 0:
        return '{"status": "400", "msg": "Product with that name already exists"}', 400

    db.execute(f"INSERT INTO current_stock (name, quantity) VALUES ('{response["name"]}', 0)")
    conn.commit()

    return "200 OK"