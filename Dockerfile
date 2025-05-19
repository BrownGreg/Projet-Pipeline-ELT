FROM python:3.10-slim

WORKDIR /app

COPY scripts/ scripts/

RUN pip install --no-cache-dir pandas psycopg2-binary sqlalchemy python-dotenv black bandit

CMD ["python", "scripts/orchestrator.py"]
