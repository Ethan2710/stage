import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la fenêtre de jeu
screen = pygame.display.set_mode((800, 600))

# Définition du fond
fond = pygame.Surface((800, 600))
fond.fill((135, 206, 235))  # couleur du fond

# Définition des nuages
nuages = []
for i in range(10):
    nuage = pygame.Rect(i * 100, 100, 50, 50)
    nuages.append(nuage)

# Définition de la vitesse de déplacement du fond
vitesse_fond = 2

# Création du personnage
personnage = pygame.Rect(100, 100, 50, 50)
personnage_image = pygame.Surface((50, 50))  # créer une surface de 50x50 pixels
personnage_image.fill((255, 0, 0))  # remplir la surface de rouge

# Boucle de jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                personnage.x -= 5
            elif event.key == pygame.K_RIGHT:
                personnage.x += 5
            elif event.key == pygame.K_UP:
                personnage.y -= 5
            elif event.key == pygame.K_DOWN:
                personnage.y += 5

    # Déplacement du fond
    for nuage in nuages:
        nuage.x -= vitesse_fond
        if nuage.x < -50:
            nuage.x = 800

    # Dessin du fond
    screen.blit(fond, (0, 0))

    # Dessin des nuages
    for nuage in nuages:
        pygame.draw.rect(screen, (255, 255, 255), nuage)

    # Dessin du personnage
    screen.blit(personnage_image, personnage)

    # Mise à jour de l'écran
    pygame.display.flip()

    # Gestion du temps
    pygame.time.Clock().tick(60)
