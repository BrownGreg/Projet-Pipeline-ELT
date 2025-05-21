import time
import subprocess
import logging
import os
import sys
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
load_dotenv()


def run_extract_load():
    logging.info("Lancement de l'ingestion des données brutes...")
    script_path = os.path.abspath("scripts/extract_load.py")
    result = subprocess.run(
        [sys.executable, script_path], capture_output=True, text=True
    )
    if result.returncode == 0:
        logging.info("Ingestion réussie.")
    else:
        logging.error("Erreur pendant l'ingestion :\n%s", result.stderr)


def run_sql_transformations():
    logging.info("Exécution des transformations SQL...")

    env = os.environ.copy()
    env["PGPASSWORD"] = os.getenv("DB_PASSWORD")

    psql_path = "/usr/bin/psql"  # Adapter si besoin selon l'image Docker
    psql_cmd = [
        psql_path,
        "-h", os.getenv("DB_HOST"),
        "-U", os.getenv("DB_USER"),
        "-d", os.getenv("DB_NAME"),
        "-f", os.path.abspath("sql/transformations.sql"),
    ]
    result = subprocess.run(psql_cmd, capture_output=True, text=True, env=env)

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
