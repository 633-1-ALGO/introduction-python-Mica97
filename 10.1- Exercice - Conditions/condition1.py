# Problème : Etant donné deux variables c et d, on veut savoir si leur produit est négatif ou positif ou nul.
# Contrainte : Ne pas calculer le produit des deux nombres.
# Résultat attendu : Un message affichant "Produit positif" ou "Produit négatif" ou "Produit nul".
# Indications :  Vous pouvez changer les valeurs des variables pour vos tests.
c = 1
d = -5

prod = c*d

if prod > 0:
    print("Produit positif")
elif prod < 0:
    print("Produit négatif")
else:
    print("Nul")
