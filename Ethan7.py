from math import *
import unittest
print('Nous allons vous claculer l aire d un triangle en m² et son périmètre en m')
d = int(input("choisissez un nombre entier pour une longueur d un demi-périmètre : "))
a = int(input("choisissez un nombre entier pour la longueur du premier coté du triangle : "))
b = int(input("choisissez un nombre entier pour la longueur du deuxieme coté du triangle : "))
c = int(input("choisissez un nombre entier pour la longueur du dernier coté du triangle : "))
périmètre = a + b + c
def triangle(d,a,b,c):
    return (d*(d-a)*(d-b)*(d-c))
class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(triangle(10, 3, 4, 5), 6) 
        self.assertEqual(triangle(-1, 1, 1, 1), None)
        self.assertEqual(triangle(0, 0, 0, 0), None)
expression = int(d)*(int(d)-int(a))*(int(d)-int(b))*(int(d)-int(c))
if expression < 0:
    print("Erreur : l'aire du triangle est négative")
    aire = None
else:
    aire = (sqrt(expression))
print('Le périmètre du triangle est',périmètre, 'm')
print('L aire du triangle est',aire, 'm2')