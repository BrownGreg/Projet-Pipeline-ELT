import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        print("✅ Connexion réussie à PostgreSQL")
        conn.close()
    except Exception as e:
        print("❌ Échec de la connexion :", e)

if __name__ == "__main__":
    test_connection()
