import unittest
from jeu import pygame

class TestPersonnageRebond(unittest.TestCase):
    def test_rebond_gauche(self):
        # Définir la position du personnage sur le bord gauche de l'écran
        personnage_x = 0
        personnage_y = 100

        # Simuler un déplacement vers la gauche
        personnage_x -= 5

        # Vérifier que le personnage rebondit sur le bord gauche
        self.assertGreaterEqual(personnage_x, 0)

    def test_rebond_droit(self):
        # Définir la position du personnage sur le bord droit de l'écran
        personnage_x = 800 - 50
        personnage_y = 100

        # Simuler un déplacement vers la droite
        personnage_x += 5

        # Vérifier que le personnage rebondit sur le bord droit
        self.assertLessEqual(personnage_x, 800 - 50)

    def test_rebond_haut(self):
        # Définir la position du personnage sur le bord haut de l'écran
        personnage_x = 100
        personnage_y = 0

        # Simuler un déplacement vers le haut
        personnage_y -= 5

        # Vérifier que le personnage rebondit sur le bord haut
        self.assertGreaterEqual(personnage_y, 0)

    def test_rebond_bas(self):
        # Définir la position du personnage sur le bord bas de l'écran
        personnage_x = 100
        personnage_y = 600 - 50

        # Simuler un déplacement vers le bas
        personnage_y += 5

        # Vérifier que le personnage rebondit sur le bord bas
        self.assertLessEqual(personnage_y, 600 - 50)

if __name__ == '__main__':
    unittest.main()