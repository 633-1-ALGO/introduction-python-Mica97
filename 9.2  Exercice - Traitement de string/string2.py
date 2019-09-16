# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

occu = texte.count("exemple")

print("Nombre d'occurences de 'Exemple' : ",occu)

texte.replace("est", "représente")

print("Texte remplacé",texte)
