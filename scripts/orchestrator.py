import time
import subprocess
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
load_dotenv()


def run_extract_load():
    logging.info("Lancement de l'ingestion des données brutes...")
    result = subprocess.run(
        ["python", "scripts/extract_load.py"], capture_output=True, text=True
    )
    if result.returncode == 0:
        logging.info("Ingestion réussie.")
    else:
        logging.error("Erreur pendant l'ingestion :\n%s", result.stderr)


def run_sql_transformations():
    logging.info("Exécution des transformations SQL...")

    env = os.environ.copy()
    env["PGPASSWORD"] = os.getenv("DB_PASSWORD")

    psql_cmd = [
        "psql",
        "-h",
        os.getenv("DB_HOST"),
        "-U",
        os.getenv("DB_USER"),
        "-d",
        os.getenv("DB_NAME"),
        "-f",
        "sql/transformations.sql",
    ]

    result = subprocess.run(psql_cmd, env=env, capture_output=True, text=True)

    if result.returncode == 0:
        logging.info("Transformations SQL exécutées avec succès.")
    else:
        logging.error("Erreur SQL :\n%s", result.stderr)


if __name__ == "__main__":
    logging.info("=== PIPELINE ELT - Démarrage ===")
    start = time.time()

    run_extract_load()
    run_sql_transformations()

    end = time.time()
    duration = end - start

    os.makedirs("logs", exist_ok=True)
    with open("logs/report.txt", "w") as f:
        f.write(f"✅ Pipeline terminé en {duration:.2f} secondes.\n")

    logging.info("=== PIPELINE ELT - Terminé ===")
