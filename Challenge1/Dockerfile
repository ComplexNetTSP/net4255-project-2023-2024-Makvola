# Utiliser l'image officielle Python comme image de base
FROM python:3

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le code Flask dans le répertoire de travail
COPY app.py .
COPY templates/ templates

# Installer les dépendances Flask
RUN pip install Flask

# Exposer le port sur lequel l'application Flask sera accessible
EXPOSE 5000

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=app.py

# Définir la commande à exécuter lorsque le conteneur démarre
CMD ["flask", "run", "--host=0.0.0.0"]
