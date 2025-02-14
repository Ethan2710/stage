import pygame

# Initialiser Pygame
pygame.init()

import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Définition de la barrière
barriere_width = 799
barriere_height = 799
barriere_x = (screen_width - barriere_width) / 2
barriere_y = (screen_height - barriere_height) / 2

# Définition du personnage
personnage_width = 50
personnage_height = 50
personnage_x = 100
personnage_y = 100
personnage_speed = 5

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacement du personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        personnage_y -= personnage_speed
    if keys[pygame.K_DOWN]:
        personnage_y += personnage_speed
    if keys[pygame.K_LEFT]:
        personnage_x -= personnage_speed
    if keys[pygame.K_RIGHT]:
        personnage_x += personnage_speed

    # Collision avec la barrière
    if (personnage_x + personnage_width > barriere_x and
            personnage_x < barriere_x + barriere_width and
            personnage_y + personnage_height > barriere_y and
            personnage_y < barriere_y + barriere_height):
            # Repousse le personnage
            if keys[pygame.K_UP]:
                personnage_y += personnage_speed
            if keys[pygame.K_DOWN]:
                personnage_y -= personnage_speed
            if keys[pygame.K_LEFT]:
                personnage_x += personnage_speed
            if keys[pygame.K_RIGHT]:
                personnage_x -= personnage_speed

        # Dessin de la barrière et du personnage
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (barriere_x, barriere_y, barriere_width, barriere_height))
    pygame.draw.rect(screen, (255, 0, 0), (personnage_x, personnage_y, personnage_width, personnage_height))


    # Définir la taille de la fenêtre
    WIDTH = 800
    HEIGHT = 600

    # Créer la fenêtre
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    # Définir le fond d'écran
    background = pygame.Surface(window.get_size())
    background.fill((255, 255, 255))

    # Définir la vitesse du personnage
    player_speed = 0.5

    # Définir la position initiale du personnage
    player_x = WIDTH // 2
    player_y = HEIGHT - 50

    # Définir la taille du personnage
    player_width = 50
    player_height = 50

    # Définir la couleur du personnage
    player_color = (255, 0, 0)

    # Boucle principale du jeu
    running = True
    while running:
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Gérer les entrées du clavier
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Dessiner le fond d'écran
        window.blit(background, (0, 0))

        # Dessiner le personnage
        pygame.draw.rect(window, player_color, (player_x, player_y, player_width, player_height))

        # Mettre à jour l'écran
        pygame.display.flip()

    # Quitter le jeu
    pygame.quit()