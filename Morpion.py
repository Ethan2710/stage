# Tic-Tac-Toe

# La grille de jeu
grille = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# La fonction pour afficher la grille
def afficher_grille():
    print(" " + grille[0][0] + " | " + grille[0][1] + " | " + grille[0][2])
    print("---+---+---")
    print(" " + grille[1][0] + " | " + grille[1][1] + " | " + grille[1][2])
    print("---+---+---")
    print(" " + grille[2][0] + " | " + grille[2][1] + " | " + grille[2][2])

# La fonction pour vérifier si un joueur a gagné
def verifier_gagne(joueur):
    # Vérifier les lignes
    for i in range(3):
        if grille[i][0] == joueur and grille[i][1] == joueur and grille[i][2] == joueur:
            return True
    # Vérifier les colonnes
    for i in range(3):
        if grille[0][i] == joueur and grille[1][i] == joueur and grille[2][i] == joueur:
            return True
    # Vérifier les diagonales
    if (grille[0][0] == joueur and grille[1][1] == joueur and grille[2][2] == joueur) or \
       (grille[0][2] == joueur and grille[1][1] == joueur and grille[2][0] == joueur):
        return True
    return False

# La fonction pour jouer un tour
def jouer_tour(joueur):
    afficher_grille()
    print("Joueur", joueur, "à votre tour.")
    ligne = int(input("Entrez le numéro de la ligne (1-3) : ")) - 1
    colonne = int(input("Entrez le numéro de la colonne (1-3) : ")) - 1
    if grille[ligne][colonne] != " ":
        print("Cette case est déjà occupée.")
        jouer_tour(joueur)
    else:
        grille[ligne][colonne] = joueur
        if verifier_gagne(joueur):
            afficher_grille()
            print("Joueur", joueur, "a gagné !")
            exit()
        else:
            jouer_tour("X" if joueur == "O" else "O")

# Le jeu commence
jouer_tour("X")