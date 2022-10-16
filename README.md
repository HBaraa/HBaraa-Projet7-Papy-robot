# Projet 7:

# Créez GrandPy Bot, le papy-robot
==============================================

## Présentation du projet:

l'idée du projet est de concevoir et mettre en place une application web qui consiste à demander à un papy robot nommé Grandpy l'adresse d'un endroit. Ce dernier retourne l'adresse demandée avec une carte Google Maps qui apparaît également avec un marqueur indiquant l'endroit cherché.
Afin d'ajouter un aspect humanoid à Grandpy, en affichant l'adresse, papy raconte de sa douce manière une anecdote sur cet endroit afin de montrer à l'utilisateur qu'il est doué pour échanger avec lui et qu'il essaye autant que possible de l'aider et s'il ne trouve pas l'adresse c'est que l'utilisatteur a fait une mauvaise saisie.

## Utilisation de l'application:

Afin d'utiliser l'application, il faut suivre les étapes suivantes;
- Installer python 3.9
- Cloner le projet depuis le repository Github
- A la racine du projet :
 ```
python -m venv .venv  # ou python3 -m venv .venv
source .venv/Scripts/activate  # .venv/bin/activate on linux
pip install -r requirements.txt  # installation des dépendances
```
- Générer une clés ( `SECRET_API_KEY`) de Google API
- Instancier votre clé d'API Google en tant que variable d'environnement dans la console sous l'environnement virtuel toujours actif (Attention cette variable doit s'appeler impérativement `SECRET_API_KEY`)
- Taper ces trois commandes dans le terminal;
 ```
export FLASK_APP=app_folder.views.py
export FLASK_ENV=developement
flask run
```
- Ouvrez l'application web en local : `http://127.0.0.1:5000 `.

###    ==>  Have fun  ;)
