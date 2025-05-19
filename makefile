run:
	docker compose up -d

etl:
	source venv/bin/activate && python scripts/extract_load.py

init-env:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

stop:
	docker compose down

reset:
	docker compose down -v
	rm -rf venv __pycache__

logs:
	docker compose logs -f postgres

check:
	black scripts/
	bandit -r scripts/