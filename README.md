# Formation-unil



## Dates et description des modules
 

les séances ont lieu en ligne de 17h à 19h 
 

### 11.03 - module d'introduction: les bases de la programmation en Python

 
Cette première séance propose d'aborder les raisons de faire du script scientifique pour manipuler des données et la pertinence d'utiliser Python. Nous aborderons l'usage du Notebook Jupyter, la structuration d'un script, la grammaire de Python et nous verrons les bases nécessaires pour faire du recodage de données stockées dans un fichier.
 

### 25.03 - traitement de données basiques : la bibliothèque Pandas
 

Cette séance propose de montrer tout l'intérêt de combiner l'usage d'un tableur comme Excel et la programmation Python grâce à la bibliothèque Pandas pour traiter les données. Nous verrons comment ouvrir un fichier tableur, manipuler les colonnes, faire des calculs et des représentations graphiques.

 

### 15.04 - statistique descriptives et inférentielles

 

Cette séance vise à faire le tour de la boîte à outils de statistiques classiques du chercheur en SHS, mais aussi les représentations graphiques. Moyenne, tableau croisé, corrélation, régression linéaire et diagrammes divers, l'objectif est de vous montrer que vous pouvez retrouver tous les traitements habituels, et intégrer ces traitements de manière fluide dans votre réflexion en gardant une trace des différentes étapes pour pouvoir les partager.

 

### 29.04 - modèles avancés : régressions, clustering et prédiction

 

Cette séance prolonge la séance sur les statistiques pour s'intéresser aux traitements plus avancés ainsi que leurs bibliothèques. Nous verrons comment réaliser une régression logistique et un clustering sur des données, mais aussi présenter les données pour les interpréter ensuite.

 

### 20.05 - collecter les données sur internet et s’interfacer avec des API

 

Cette  séance se concentre sur l'utilisation de la programmation Python pour collecter des données sur internet. Dans de nombreux cas, des interfaces existent (des API) avec des bibliothèques dédiées (Wikipédia, Google Trends ou Twitter par exemple). Dans d'autres cas, il est nécessaire de collecter des pages internet et de les décomposer. 


### 27.05 - construire une carte


Cette dernière séance présente l'existence de la bibliothèque GeoPandas qui permet de manipuler des données géographiques. Nous verrons comment associer des données à une carte et faire des opérations avec des dimensions géographiques.


## Préparer les séances

### Rapide panorama

Python est un langage interprété qui nécessite un environnement. 

Il existe plusieurs manières de l'utiliser :
- Sur votre ordinateur, avec Anaconda (ci-dessous)
- Sur le Cloud, avec différentes solutions, par exemple Google colab https://colab.research.google.com/

Pour les premières séances, le Cloud est une solution souple qui évite l'installation.


### Installation d'Anaconda

Anaconda est un environnement qui fournit l'ensemble des éléments nécessaires pour exécuter du code python. Il permet de construire des environnements (une version du langage et de librairies spécifiques) et de travailler au sein de ces environnements permettant d'en avoir plusieurs (par exemple, pour tester des versions différentes de librairies, etc.)

- Télécharger Anaconda pour votre OS : https://www.anaconda.com/distribution/
- Installer (suivant que vous soyez sous Windows, Linux ou Mac, la procédure va changer)
- Lancer Anaconda pour créer un environnement de travail
  - Sur windows : Aller dans environnements > Create > donner un nom (ex. p37) et une version de python 3.7 (__Attention bien installer la version 3.7 ou plus de Python __)
  - Sur linux/mac : Ouvrir un terminal, puis créer un environnement en tappant la commande : conda create --name p37 python=3.7 (pour toute information sur les commandes conda : https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- Lancer python (sur windows en lançant Anaconda ; sous linux/mac en tapant la commande source activate p37 dans un terminal)
- lancez un terminal (vous pouvez le faire sous le logiciel Anaconda) et vérifiez que ipython est bien installé en tapant ipython de manière similaire, lancez Jupyter notebook en tapant jupyter notebook


Autres logiciels

Vous pouvez installer Sublime text : https://www.sublimetext.com/ (pour visualiser des documents textes)
