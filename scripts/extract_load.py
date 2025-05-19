import os
import logging
import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_PARAMS = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

for key, value in DB_PARAMS.items():
    if value is None:
        logging.error(f"Variable d'environnement manquante : {key}")
        raise EnvironmentError(f"Missing required DB config: {key}")
    if key == "password":
        logging.info(f"{key} = ********")
    else:
        logging.info(f"{key} = {value}")

CSV_PATH = "data/raw/cars_dataset.csv"

try:
    df = pd.read_csv(CSV_PATH)
    df.columns = df.columns.str.strip().str.lower()  # normalisation
    logging.info(f"Fichier CSV chargé avec succès : {CSV_PATH} ({len(df)} lignes)")
    logging.info(f"Colonnes détectées : {df.columns.tolist()}")
except FileNotFoundError:
    logging.error(f"File not found : {CSV_PATH}")
    raise
except Exception as e:
    logging.error(f"Erreur lors du chargement CSV : {e}")
    raise

try:
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    logging.info("Connexion à PostgreSQL réussie")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS raw_cars (
            id SERIAL PRIMARY KEY,
            model TEXT,
            year INT,
            price FLOAT,
            transmission TEXT,
            mileage INT,
            fueltype TEXT,
            tax FLOAT,
            mpg FLOAT,
            enginesize FLOAT,
            make TEXT
        );
    """)

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO raw_cars (
                model, year, price, transmission,
                mileage, fueltype, tax, mpg, enginesize, make
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row.get("model"),
            row.get("year"),
            row.get("price"),
            row.get("transmission"),
            row.get("mileage"),
            row.get("fueltype"),
            row.get("tax"),
            row.get("mpg"),
            row.get("enginesize"),
            row.get("make")
        ))

    conn.commit()
    logging.info(f"Données insérées avec succès dans la table raw_cars")

except Exception as e:
    logging.error(f"Erreur PostgreSQL : {e}")
    raise
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
        logging.info("Connexion PostgreSQL fermée")
