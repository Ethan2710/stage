from math import *
d = input('choisissez un nombre entier pour une longueur d un demi-périmètre ')
a = input('choisissez un nombre entier pour une longueur d un coté du triangle ')
b = input('choisissez un nombre entier pour une longueur d un autre coté du triangle ')
c = input('choisissez un nombre entier pour une longueur d un autre coté du triangle ')
périmètre = a + b + c
expression = int(d)*(int(d)-int(a))*(int(d)-int(b))*(int(d)-int(c))

if expression < 0:
    print("Erreur : l'expression est négative")
    aire = None
else:
    aire = (sqrt(expression))
print(périmètre)
print(aire)