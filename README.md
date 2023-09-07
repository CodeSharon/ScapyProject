## Prérequis

- Python 3.x
- Django

## Installation

- Clonez cette repos  : git clone https://github.com/CodeSharon/ScapyProject.git 

## Configuration

1. Assurez-vous d'avoir une base de données configurée et migrez les modèles 

- python3 manage.py makemigrations
- python3 manage.py migrate

2. Créez un superutilisateur pour accéder à l'interface d'administration et a la listes des demandes de capture (en tant qu'expert) :

- python3 manage.py createsuperuser

## Lancement du serveur django (en root)

- python3 manage.py runserver

## Utilisation

1. Authentification en tant qu'analyseur

- Sur la page login "http://localhost:8000/analyzer/login", vous pouvez directement créer un utilisateur en saisissant un <nom utilisateur> et un <mot de passe> afin de faire des demandes.

2. Authentification en tant qu'expert

- S'authentifier avec les credentials du superuser pour avoir accès aux demandes de captures.
