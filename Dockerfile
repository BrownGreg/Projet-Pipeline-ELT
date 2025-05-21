FROM python:3.10-slim

WORKDIR /app

COPY scripts/ scripts/
COPY sql/ sql/
COPY data/raw/cars_dataset.csv data/raw/cars_dataset.csv
#COPY requirements.txt .

RUN apt update && apt install -y postgresql-client
RUN pip install --no-cache-dir pandas psycopg2-binary sqlalchemy python-dotenv black bandit

CMD ["python", "scripts/orchestrator.py"]
