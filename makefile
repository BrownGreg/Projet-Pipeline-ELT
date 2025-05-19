# Makefile - Exécution rapide

run: 
	docker compose up -d

etl:
	source venv/bin/activate && python orchestrator.py

init-env:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

stop:
	docker compose down

reset:
	docker compose down -v
	rm -rf venv __pycache__

logs:
	docker logs hetic_postgres
