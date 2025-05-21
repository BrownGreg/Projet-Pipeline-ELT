import os
import psycopg2
import pytest
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.test", override=True)


@pytest.mark.skipif(os.getenv("SKIP_DB_TESTS") == "1", reason="PostgreSQL non disponible")
def test_postgres_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        conn.close()
        assert True
    except Exception:
        assert False, "Connexion à PostgreSQL échouée"
