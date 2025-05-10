import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Application de dessin")


current_color = (255, 0, 0)  
background_color = (255, 255, 255)  
screen.fill(background_color)

# Epaisseur du pinceau
brush_size = 5

def draw_circle(pos, color):
    pygame.draw.circle(screen, color, pos, brush_size)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_r:
                current_color = (255, 0, 0)  
            elif event.key == pygame.K_g:
                current_color = (0, 255, 0) 
            elif event.key == pygame.K_b:
                current_color = (0, 0, 255) 
            elif event.key == pygame.K_e:
                screen.fill(background_color)  
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            draw_circle(pos, current_color)

    pygame.display.flip()


