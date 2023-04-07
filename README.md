# Welcome to Datalake project!

Bonjour, nous sommes l'équipe du Master Business Intelligence & Analytics composé de Kouseila Ouagheni, Michel Bataillon et d'Anthony Marais.

Dans ce projet, nous traitons des données non structurées depuis leur fichier brut 'html' jusqu'à l'analyse des données dans un outil BI.


# Installation du projet

Tout d'abord, veuillez télécharger le projet :
> git clone  https://github.com/anthony-marais/TD_DATALAKE.git


Une fois, le projet téléchargé merci de bien vouloir le placer dans un répertoire spécifique sur votre poste de travail :

- Windows :
> 'C:/' 

Le chemin du projet devrait ressembler à celui-ci : 
> 'C:/TD_DATALAKE'
- Linux où MacOS :
> 'home/{USER}/Documents' 

{USER} correspondant au nom de l'utilisateur de la machine. Le répertoire du projet devrait ressembler à celui-ci :
> '/home/{USER}/Documents/TD_DATALAKE'


## Création de l'environnement virtuel Python

Pour ce projet, vous aurez besoin de librairies spécifiques au bon fonctionnement du projet, pour ce faire nous vous proposons de créer un environnement virtuel et d'installer les packages dédiés pour ce projet.
Dans le répertoire du projet, veuillez créer votre environnement virtuel.

- Windows :
dans le répertoire 'C:/TD_DATALAKE'
> python -m venv venv
>
Pour activer l'environnement, il vous suffira de taper cette commande :
> venv\Scripts\activate

Si l'activation ne s'effectue pas correctement, il suffira de suivre la documentation proposée par Microsoft

-Linux où MacOS
dans le répertoire  '/home/{USER}/Documents/TD_DATALAKE'
> venv/bin/activate 


## Installation des librairies du projet

Une fois votre environnement virtuel créé et activé, nous allons installer les librairies du projet, toujours dans le répertoire de travail du projet un fichier **requirements.txt** contenant toutes les librairies nécessaire au bon fonctionnement du projet.

Que ce soit sous Linux, Windows où MacOS l'installation est identiques :
> pip install -r requirements.txt

## Renommage du fichier .env

Pour le bon fonctionnement du projet un fichier .env est nécessaire, celui-ci contient de nombreuses variables de contextes du projet. 

Lors du partage des sources sur GitHub l'une des bonne pratique mise en place est de ne pas 'Push' le fichier .env du projet, mais d'en envoyer un fichier exemple.

Dans le répertoire **'TD_DATALAKE/DVLP/CODING'** vous trouverais un fichier nommé **'.env copy'** renommez le en : **'.env'**.

## Lancement du programme

Le fichier main.py dans le répertoire  **'TD_DATALAKE/DVLP/CODING'** contient le code pour lancer l'ensemble du projet.

Lors du lancement un petit menu apparaitra pour vous permettre de selectionner la tâche spécifique que vous voulez effectuer :

>1. Move file from source to landing zone
>2. Get data from Linkedin
>3. Get data from Glassdoor avis
>4. Get data from Glassdoor society
