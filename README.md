# Projet Pipeline ELT

🌍 **Contexte**  
Ce projet a été réalisé dans le cadre du module "Data Engineering" à HETIC (promo DIA2). Il consiste à créer un pipeline ELT complet de l’ingestion à la modélisation, en utilisant un dataset libre sur les voitures.

📚 **Objectifs du projet**  
- Ingestion de données brutes à partir d’un fichier CSV
- Stockage dans PostgreSQL via Docker
- Transformation et modélisation des données en base
- Orchestration automatique du pipeline
- Documentation claire et livrables prêts pour soutenance

⚙️ **Technologies utilisées**  
- **Python** : ingestion, orchestration
- **PostgreSQL** : base de données relationnelle
- **Docker** : environnement de base de données isolé
- **psycopg2-binary / pandas / sqlalchemy** : connexion et manipulation de données
- **SQL** : création des tables et transformations
- **dotenv / Makefile / logging / time** : gestion d’environnement, automatisation, journalisation

## 🎓 **Installation du projet**

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

### 3. Vérification des données après transformation:
```bash
psql -d cars_project -c "SELECT * FROM fact_car_sales LIMIT 10;"
```

### 4. Ou via le Makefile :
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

##Modélisation des données

Le modèle des données utilisé dans ce projet suit une structure en étoile avec des tables dimensionnelles et une table des faits. Voici un aperçu des tables et de leurs relations :

```
dim_make : Table contenant les marques de voitures

make_id : Clé primaire

make_name : Nom de la marque (ex : BMW, Audi, etc.)

dim_model : Table contenant les modèles de voitures

model_id : Clé primaire

model_name : Nom du modèle (ex : X5, A4, etc.)

make_id : Clé étrangère, référence à dim_make

dim_transmission : Table contenant les types de transmission

transmission_id : Clé primaire

transmission_type : Type de transmission (ex : Manual, Automatic)

dim_fuel : Table contenant les types de carburant

fuel_id : Clé primaire

fuel_type : Type de carburant (ex : Petrol, Diesel)

fact_car_sales : Table de faits qui relie les dimensions et contient les mesures

sale_id : Clé primaire

make_id : Clé étrangère, référence à dim_make

model_id : Clé étrangère, référence à dim_model

transmission_id : Clé étrangère, référence à dim_transmission

fuel_id : Clé étrangère, référence à dim_fuel

year, price, mileage, tax, mpg, engine_size : Mesures des ventes
```

Les relations entre ces tables permettent d'analyser les ventes de voitures par marque, modèle, transmission, carburant, et autres critères. Un schéma ER de la base de données est disponible dans le dossier docs/.

---

## 🧰 Equipe

- **Grégory** : Orchestration & Ingestion
- **Othmane** : Modélisation & SQL
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

---

## Conclusion
Voici un README.md complet qui couvre tous les aspects du projet : installation, utilisation, structure, technologies, et documentation technique pour la modélisation.
