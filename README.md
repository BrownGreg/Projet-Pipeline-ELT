# Projet-Pipeline-ELT

git clone https://github.com/ton-org/Projet-Pipeline-ELT.git
cd Projet-Pipeline-ELT
cp .env.example .env

docker compose up -d


python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


python scripts/extract_load.py
