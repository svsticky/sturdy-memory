import psycopg2

conn = psycopg2.connect(
    database="stocky",
    host="192.168.1.136",
    user="dev",
    password="dev",
    port="5432"
)

db = conn.cursor()

def setup_table():
    try:
        db.execute("""
create table current_stock
(
    id       bigserial
        constraint primary_key
            primary key,
    name     varchar(64)       not null,
    quantity integer default 0 not null
);

alter table current_stock
    owner to dev;
        """)
    except psycopg2.errors.DuplicateTable:
        print("Table already exists.")
    conn.commit()
