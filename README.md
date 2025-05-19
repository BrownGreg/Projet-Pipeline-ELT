# Projet Pipeline ELT

## 🌍 Contexte
Ce projet a été réalisé dans le cadre du module "Data Engineering" à HETIC (promo DIA2).
Il consiste à créer un pipeline ELT complet de l’ingestion à la modélisation, en utilisant un dataset libre sur les voitures.

---

## 📚 Objectifs du projet

- Ingestion de données brutes à partir d’un fichier CSV
- Stockage dans PostgreSQL via Docker
- Transformation et modélisation des données en base
- Orchestration automatique du pipeline
- Documentation claire et livrables prêts pour soutenance

---

## ⚙️ Technologies utilisées

- **Python** : ingestion, orchestration
- **PostgreSQL** : base de données relationnelle
- **Docker** : environnement de base de données isolé
- **psycopg2-binary / pandas / sqlalchemy** : connexion et manipulation de données
- **SQL** : création des tables et transformations
- **dotenv / Makefile / logging / time** : gestion d’environnement, automatisation, journalisation

---

## 🤖 Installation du projet

### 1. Cloner le repo
```bash
git clone https://github.com/votre-utilisateur/Projet-Pipeline-ELT.git
cd Projet-Pipeline-ELT
```

### 2. Initialiser l’environnement
```bash
cp .env.example .env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Lancer PostgreSQL avec Docker
```bash
docker compose up -d
```

---

## 🎓 Utilisation du pipeline

### 1. Ingestion simple (brute)
```bash
python scripts/extract_load.py
```

### 2. Orchestration complète (ingestion + transformations)
```bash
python scripts/orchestrator.py
```

### 3. Ou via le Makefile :
```bash
make run       # Lance docker
make etl       # Lance le pipeline complet
make stop      # Stoppe les conteneurs
make reset     # Stoppe tout + supprime les volumes
```

Un rapport automatique est généré dans `logs/report.txt` à chaque exécution.

---

## 📊 Structure du projet

```
Projet-Pipeline-ELT/
├── data/raw/                # Données sources (non versionnées)
├── docs/                    # Schémas, présentation, PPT
├── scripts/                 # Scripts Python : ingestion + orchestration
├── sql/                    # Création des tables et transformations
├── logs/                   # Logs d'exécution et rapports
├── .env.example            # Variables d’environnement (exemple)
├── docker-compose.yml      # Conteneur PostgreSQL
├── Makefile                # Automatisation
├── requirements.txt        # Packages Python
└── README.md               # Ce fichier
```

---

## 🧰 Equipe

- **Grégory** : Orchestration & Ingestion
- **Othmann** : Modélisation & SQL
- **Lucien** : Documentation & Présentation

---

## ✅ Livrables attendus

- [x] Code source (Python, SQL) via GitHub
- [x] Fichier `.env.example` et `README.md`
- [x] Schéma du pipeline (`docs/schema_pipeline.png`)
- [x] Schéma BDD (`docs/schema_bdd.png`)
- [x] `presentation.pptx` pour soutenance (max 10 min)

---

## 🔒 Notes

- Ne pas versionner `.env` ni `venv/`
- Docker doit être configuré avec WSL2 sur chaque poste
- PostgreSQL tourne sur `localhost:5432` par défaut
- Vérifier les ports et configurations dans `docker-compose.yml`
- Les logs sont générés dans `logs/` pour chaque exécution

