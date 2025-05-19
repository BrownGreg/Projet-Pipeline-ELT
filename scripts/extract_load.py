import pandas as pd
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Charger les variables d’environnement
load_dotenv()

DB_PARAMS = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "dbname": os.getenv("DB_NAME", "elt_project"),
    "user": os.getenv("DB_USER", "hetic"),
    "password": os.getenv("DB_PASSWORD", "hetic123")
}

CSV_PATH = "/home/browngreg/Hetic/DataEng/Projet-Pipeline-ELT/data/cars_dataset.csv"


# Lecture des données
df = pd.read_csv(CSV_PATH)

# Connexion à PostgreSQL
conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

# Création de la table raw
cur.execute("""
    DROP TABLE IF EXISTS raw_cars;
    CREATE TABLE raw_cars (
        model TEXT,
        year INT,
        price INT,
        transmission TEXT,
        mileage INT,
        fuelType TEXT,
        tax FLOAT,
        mpg FLOAT,
        engineSize FLOAT,
        make TEXT
    );
""")
conn.commit()

# Insertion des données
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO raw_cars (model, year, price, transmission, mileage, fuelType, tax, mpg, engineSize, make)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("✅ Données insérées dans la table raw_cars.")
