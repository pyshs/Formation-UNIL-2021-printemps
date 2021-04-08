# Exercices

## Séance 2

1. Écrire un script qui stocke dans un fichier les titres d'articles contenus dans le fichier articles_ig_monde.csv qui comprennent le terme "islamo"
2. Écrire une fonction qui compte le nombre de mots de plus de deux lettres contenu dans une phrase
3. Modifier la fonction précédente pour qu'elle compte le nombre de mots uniques de la phrase


## De la séance 2 à la séance 3

vous avez un jeu de données (compressées, donc à décompresser) qui contiennent tous les articles du Monde, quotidien français, sur une période, mentionnant le terme "islamogauchisme". 

L'objectif est de construire un unique fichier CSV qui comprend : la date de l'article, son titre, le nombre de mots qu'il contient, et le nombre de fois où le terme "islamogauchisme" ou "islamo-gauchisme" est contenu. 

[vous avez toutes les briques de base pour faire cela, sauf peut-être le module os, à importer (import os), et qui a une fonction listant le contenu d'un dossier (os.listdir("./dossier"))].