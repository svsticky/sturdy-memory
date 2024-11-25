import psycopg2

# TODO Add these into a .env file, this is suboptimally secure :)
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
CREATE TABLE Producten (
    Product_ID SERIAL PRIMARY KEY,
    Product_Naam VARCHAR(255) NOT NULL,
    Product_Aantal INT NOT NULL,
    Product_Barcode VARCHAR(255)
);

CREATE TABLE Transacties (
    Transactie_ID SERIAL PRIMARY KEY,
    Product_ID INT NOT NULL,
    Date_Time TIMESTAMP NOT NULL,
    Transactie_Aantal INT NOT NULL,
    FOREIGN KEY (Product_ID) REFERENCES Producten(Product_ID)
);

CREATE TABLE Derving (
    Transactie_ID INT NOT NULL,
    User_ID INT NOT NULL,
    Derving_Type VARCHAR(255),
    PRIMARY KEY (Transactie_ID, User_ID),
    FOREIGN KEY (Transactie_ID) REFERENCES Transacties(Transactie_ID)
);

CREATE TABLE Succesvolle_Transacties (
    Transactie_ID INT PRIMARY KEY,
    FOREIGN KEY (Transactie_ID) REFERENCES Transacties(Transactie_ID)
);
        """)
    except psycopg2.errors.DuplicateTable:
        print("Table already exists.")
    conn.commit()
