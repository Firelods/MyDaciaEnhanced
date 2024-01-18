FROM python:3.10-slim
LABEL authors="Clement"

WORKDIR /code

# Copier le fichier requirements.txt pour les dépendances de python dans l'image
COPY requirements.txt .
# Copier le script d'attente de la bdd dans l'image
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh
# Installer Netcat (version openbsd)
RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install -r requirements.txt

COPY . .
