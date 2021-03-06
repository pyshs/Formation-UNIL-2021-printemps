nombre_articles = 0
motcle = "islamo"
titres = ["Tension entre l'exécutif et le monde scientifique Après les déclarations de Vidal sur l' «  islamo-gauchisme », Attal a rappelé « l'indépendance » des chercheurs",
          "La fiche de poste modifiée de l'université Paris-Est-Créteil"]
nombre_total_articles = len(titres)
if nombre_total_articles > 0:
    for i in titres:
        if motcle in i:
            print(i)
            nombre_articles+=1
else:
	print("La liste est vide")
proportion = 100*nombre_articles/nombre_total_articles
print("Proportion d'articles contenant le terme dans le titre : {} %%".format(round(proportion,1)))