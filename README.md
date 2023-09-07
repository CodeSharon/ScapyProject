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
