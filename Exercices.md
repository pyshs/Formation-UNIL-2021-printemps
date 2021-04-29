# Exercices

## Séance 2

1. Écrire un script qui stocke dans un fichier les titres d'articles contenus dans le fichier articles_ig_monde.csv qui comprennent le terme "islamo"
2. Écrire une fonction qui compte le nombre de mots de plus de deux lettres contenu dans une phrase
3. Modifier la fonction précédente pour qu'elle compte le nombre de mots uniques de la phrase


## De la séance 2 à la séance 3

vous avez un jeu de données (articles.zip ; compressées, donc à décompresser) qui contiennent tous les articles du Monde, quotidien français, sur une période, mentionnant le terme "islamogauchisme". 

L'objectif est de construire un unique fichier CSV qui comprend : la date de l'article, son titre, le nombre de mots qu'il contient, et le nombre de fois où le terme "islamogauchisme" ou "islamo-gauchisme" est contenu. 

**Aide**: vous avez toutes les briques de base pour faire cela, sauf peut-être le module os, à importer (import os), et qui a une fonction listant le contenu d'un dossier (os.listdir("./dossier")).

## Séance 3

1. Dans le tableau d'articles (corpus), ajouter une colonne qui correspond à la présence ou absence dans le titre du terme "islamo-gauchisme"
2. Est-ce que les articles qui ont le terme dans le titre ont une taille ou une fréquence du terme différents de ceux qui ne le mentionnent pas dans le titre (proposer une représentation visuelle)
3. Tracer une courbe d'évolution temporelle du nombre d'articles par journal 


## Séance 4

1. Étudier l'effet du positionnement politique sur les deux variables d'intérêt, intérêt science et apport science
2. Faire une régression logistique avec comme variable dépendante les personnes intéressées par la science
3. Proposer une analyse des réponses recodées du champ libre sur ce qu'est la science (m_q29_1 à m_q29_29) : 