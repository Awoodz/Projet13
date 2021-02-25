# Qu'est ce que c'est ?
Cette application vous permets de gérer le contenu de vos congélateurs. Elle vous permet de connaitre le contenu de l'appareil depuis n'importe quel navigateur et vous prévient quand l'un des produits approche sa durée de conservation recommandée.
Vous aurez simplement à créer des produits et des appareils puis à stocker l'un dans l'autre.

# Le contexte
Ce programme a été développé dans le cadre d'un projet proposé par OpenClassrooms afin de valider l'ensemble des compétences acquises durant la formation de développeur Python.

# Comment l'utiliser ?
### Directement sur internet !
Retrouvez l'application ici : https://mycoldmanager.herokuapp.com/

### Sur votre ordinateur :
  * Téléchargez le repository et décompressez le au chemin de votre choix
  * Assurez vous d'avoir une version récente de Python ( https://www.python.org/downloads/release )(programme developpé sous Python 3.8)
  * Installez les modules contenus dans le requirements.txt
  * Créez une variable d'environnement qui contiendra la clé secrète de l'application. Nommez la "MYCOLDMANAGER_KEY"
  * L'application utilise SendGrid (https://sendgrid.com/) pour envoyer des mails. Vous devrez vous créer un compte SendGrid et obtenir une clé api que vous placerez dans une variable d'environnement nommée "MYCOLDMANAGER_SENDGRID_KEY"
  * Téléchargez et installez Postgresql
  * Créez une base de donnée nommée "mycoldmanager" encodé en utf8 ( ```createdb -E utf8 -U postgres mycoldmanager``` )
  * Assurez vous que le port utilisé par postgresql soit le port 5432, autrement, changez le paramètre PORT de la base de donnée dans le fichier settings.py
  * Une fois votre serveur de base de donnée lancé, effectuez les migrations ( ```./manage.py migrate``` )
  * Afin de remplir la base de donnée d'éléments essentiels, lancez la commande suivante : ```./manage.py db_builder```
  * Enfin, executez la commande ```./manage.py runserver``` puis ouvrez votre navigateur web à l'adresse indiquée dans le terminal

  ### Commande spéciales :
  * ```./manage.py send_mail``` enverra des mails aux utilisateurs dont l'un des produits approche sa durée de conservation recommandée
  * ```./manage.py db_cleaner``` supprimera les plus vieilles entrées inutilisées de la base de donnée (les produits consommés depuis plus de 3 mois, etc.)
  * Note1 : Ces commandes sont automatisées sur l'application en ligne (crontask)
  * Note2 : La commande ```./manage.py db_builder``` peut être relancée pour obtenir une mise à jour des produits récupérés sur l'API OpenFoodFact