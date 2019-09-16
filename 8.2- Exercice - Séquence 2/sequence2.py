# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75
taux_tva = 7.7

prix_total_ht = nb_articles * prix_ht

Prix_TTC = prix_total_ht + (prix_total_ht * (taux_tva/100))

print("Le prix TTC est de : ", Prix_TTC , "chf")
