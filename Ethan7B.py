from math import *
print('Nous allons vous claculer le volumed un cone en mètres cube')
rayon = input('choisissez un nombre entier pour une longueur d un rayon')
hauteur = input('choisissez un nombre entier pour une longueur d une hauteur')
try:
    rayon = int(rayon)
    hauteur = int(hauteur)
    volume_cilyndre = 3.14 * rayon**2 * hauteur
except ValueError:
    print("Erreur : les valeurs de rayon et hauteur ne sont pas numériques")
volume_cône = volume_cilyndre/3
if volume_cône < 0:
    print("Erreur : l'expression est négative")
    aire = None
print('le résultat est :', volume_cône, 'm3')