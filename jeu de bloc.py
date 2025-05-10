import pygame

# Initialisation de Pygame
pygame.init()

# Constantes
LARGEUR = 800
HAUTEUR = 600
COULEUR_FOND = (30, 30, 30)
COULEUR_BLOC = (0, 200, 200)
VITESSE = 5

# Configuration de la fenêtre
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Déplacement de Bloc")

# Bloc joueur
bloc = pygame.Rect(375, 275, 50, 50)

# Boucle de jeu
jeu_en_cours = True
horloge = pygame.time.Clock()

while jeu_en_cours:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            jeu_en_cours = False

    # Gestion des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_UP]:
        bloc.y -= VITESSE
    if touches[pygame.K_DOWN]:
        bloc.y += VITESSE
    if touches[pygame.K_LEFT]:
        bloc.x -= VITESSE
    if touches[pygame.K_RIGHT]:
        bloc.x += VITESSE

    # Empêcher de sortir de l'écran
    bloc.x = max(0, min(bloc.x, LARGEUR - bloc.width))
    bloc.y = max(0, min(bloc.y, HAUTEUR - bloc.height))

    # Affichage
    ecran.fill(COULEUR_FOND)
    pygame.draw.rect(ecran, COULEUR_BLOC, bloc)
    pygame.display.flip()

    horloge.tick(60)

pygame.quit()
