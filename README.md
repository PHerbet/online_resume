# online_resume
site web avec un back django pour mettre mon cv en ligne 

Pour pouvoir utiliser TailwindCSS, assurez vous d'avoir npm et node JS d'installé sur votre ordinateur, puis, lancer la commande: 'python -m pip install -r requirements.txt' dans votre environement de travail. Ensuite, ajouter Tailwind dans les application du settings:
# settings.py
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
]
lancer la commande 'python manage.py tailwind init
'
Choisir le nom de de l'application tailwind crée,
puis l'ajouter aux applications du settings comme effectué ci dessus rajouter la variable suivante:
'# settings.py
TAILWIND_APP_NAME = 'nom_de_l_app_tailwind'
'

Pour pouvoir avoir le rafraichissement automatique du serveur, rajouter l'adresse IP de votre serveur local dans le settings:
# settings.py
INTERNAL_IPS = [
    "127.0.0.1",
]

Lancer la commande 'python manage.py tailwind install'

Puis 'python manage.py tailwind start' pour lancer le serveur tailwind.

Attention, il est parfois néccessaire de rajouter le chemin de la variable npm dans les settings, comme suit (pour windows) :
NPM_BIN_PATH =r"C:\chemin\nodejs\npm.cmd"

