# 📦 Déploiement Kubernetes du pipeline ELT

Ce document décrit comment déployer le pipeline ELT dans un cluster Kubernetes local avec Minikube.

---

## ✅ Prérequis

- Minikube installé et démarré
- Docker Desktop configuré avec WSL2
- `kubectl` et `docker` accessibles depuis WSL

---

## 🚀 Étapes de déploiement

### 1. Lancer Minikube
```bash
minikube start --driver=docker
```

---

### 2. Construire l'image Docker dans l'environnement Minikube
```bash
eval $(minikube docker-env)
docker build -t elt-orchestrator .
```

---

### 3. Déployer PostgreSQL
```bash
kubectl apply -f postgres-deployment.yaml
```

Vérifier que le pod est bien lancé :
```bash
kubectl get pods
kubectl get svc
```

---

### 4. Déployer le Job ELT (pipeline)
```bash
kubectl apply -f elt-job.yaml
```

Suivre l'exécution :
```bash
kubectl get jobs
kubectl logs -f job/elt-pipeline
```

---

## 🔁 En cas de modification du job
Supprimer l’ancien Job :
```bash
kubectl delete job elt-pipeline
```
Puis relancer :
```bash
kubectl apply -f elt-job.yaml
```

---

## 🧪 Tests et vérifications
- `orchestrator.py` doit se connecter à PostgreSQL via le **service `postgres`**
- Les variables d’environnement sont injectées dans le `elt-job.yaml`
- Les logs affichent la fin du pipeline ou les éventuelles erreurs

---

## 📂 Fichiers utilisés

| Fichier                   | Rôle                                |
|--------------------------|-------------------------------------|
| `postgres-deployment.yaml` | Déploie PostgreSQL dans Kubernetes |
| `elt-job.yaml`             | Exécute le pipeline ELT             |
| `Dockerfile`              | Image du pipeline ELT               |

---

## 💡 Astuce : ouvrir le dashboard Kubernetes
```bash
minikube dashboard
```

---

## 👥 À faire ensuite
- Ajouter un volume pour exporter les logs
- Ajouter un cronjob si besoin d’automatisation
- Ajouter un secret Kubernetes pour ne pas injecter les mots de passe en clair

---

## 🧼 Nettoyage du cluster
```bash
kubectl delete -f elt-job.yaml
kubectl delete -f postgres-deployment.yaml
```

---

## ✨ Résultat attendu
Un pipeline ELT opérationnel tournant intégralement dans un cluster Kubernetes local via Minikube.

