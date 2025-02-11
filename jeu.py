import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de l'écran
screen_width = 800
screen_height = 600

#Créer l'écran
screen = pygame.display.set_mode((screen_width, screen_height))


# Définir la position du personnage
personnage_x = 100
personnage_y = 100

# Définir la taille du personnage
personnage_width = 50
personnage_height = 50

# Créer un obstacle invisible au bord de l'écran
obstacle_x = 0
obstacle_y = 0
obstacle_width = screen_width
obstacle_height = 10

# Boucle de jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Déplacer le personnage
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        personnage_x -= 5
    if keys[pygame.K_RIGHT]:
        personnage_x += 5
    if keys[pygame.K_UP]:
        personnage_y -= 5
    if keys[pygame.K_DOWN]:
        personnage_y += 5

    # Vérifier si le personnage touche l'obstacle
    if personnage_x < obstacle_x + obstacle_width and personnage_x + personnage_width > obstacle_x and personnage_y < obstacle_y + obstacle_height and personnage_y + personnage_height > obstacle_y:
        # Repousser le personnage si il touche l'obstacle
        personnage_x = obstacle_x + obstacle_width
        personnage_y = obstacle_y + obstacle_height

    # Dessiner l'écran
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (personnage_x, personnage_y, personnage_width, personnage_height))

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
                if event.key == pygame.K_UP:
                    personnage.y -= 20
                elif event.key == pygame.K_DOWN:
                    personnage.y += 20

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

            # Définition des couleurs
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)

        # Définition de la classe Obstacle
        class Obstacle:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.width = 30
                self.height = 150
                self.speed = 5

            def draw(self):
                pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

            def update(self):
                self.x -= self.speed

        # Création de la liste des obstacles
        obstacles = []
        for i in range(10):
            x = 800 + i * 300
            y = random.randint(200, 600 - 250)
            obstacles.append(Obstacle(x, y))

        # Définition de la fonction pour vérifier les collisions
        def check_collision(x, y, obstacles):
            for obstacle in obstacles:
                if (x < obstacle.x + obstacle.width and
                    x + 50 > obstacle.x and
                    y < obstacle.y + obstacle.height and
                    y + 50 > obstacle.y):
                    return True
            return False

        # Boucle de jeu
        x = 100
        y = 100
        vitesse = 5
        game_over = False

        while True:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Déplacement du personnage
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y -= vitesse
            if keys[pygame.K_DOWN]:
                y += vitesse

            # Mise à jour des obstacles
            for obstacle in obstacles:
                obstacle.update()
                if obstacle.x < -50:
                    obstacle.x = 800
                    obstacle.y = random.randint(0, 600 - 150)

            # Vérification des collisions
            if check_collision(x, y, obstacles):
                game_over = True

            # Dessin de l'écran
            screen.fill((0, 0, 0))
            if game_over:
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over", True, WHITE)
                screen.blit(text, (350, 300))
            else:
                pygame.draw.rect(screen, WHITE, (x, y, 50, 50))
                for obstacle in obstacles:
                    obstacle.draw()
                # Vérification des collisions
                if check_collision(x, y, obstacles):
                    game_over = True

        # Dessin de l'écran
            screen.fill((0, 0, 0))
            if game_over:
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over", True, WHITE)
                screen.blit(text, (350, 300))
            else:
                pygame.draw.rect(screen, WHITE, (x, y, 50, 50))
                for obstacle in obstacles:
                    obstacle.draw()

                # Mise à jour de l'écran
                pygame.display.flip()

                # Gestion du temps
                pygame.time.Clock().tick(60)