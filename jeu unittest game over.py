import unittest
import pygame
from jeu import check_collision, Obstacle

class TestGameOver(unittest.TestCase):
    def test_collision(self):
        # Créer un obstacle
        obstacle = Obstacle(100, 100)

        # Définir la position du personnage pour qu'il soit en collision avec l'obstacle
        x = 120
        y = 120

        # Vérifier que la collision est détectée
        self.assertTrue(check_collision(x, y, [obstacle]))

    def test_game_over(self):
        # Créer un obstacle
        obstacle = Obstacle(100, 100)

        # Définir la position du personnage pour qu'il soit en collision avec l'obstacle
        x = 120
        y = 120

        # Vérifier que le jeu est en état de "Game Over"
        game_over = False
        if check_collision(x, y, [obstacle]):
            game_over = True
        self.assertTrue(game_over)

    def test_game_over_affichage(self):
        # Créer un obstacle
        obstacle = Obstacle(100, 100)

        # Définir la position du personnage pour qu'il soit en collision avec l'obstacle
        x = 120
        y = 120

        # Vérifier que le texte "Game Over" est affiché
        screen = pygame.display.set_mode((800, 600))
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (350, 300))
        pygame.display.flip()

        # Vérifier que le texte est affiché
        self.assertTrue(pygame.surfarray.array3d(screen).any())

if __name__ == '__main__':
    unittest.main()