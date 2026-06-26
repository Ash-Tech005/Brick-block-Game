import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Brick Block")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ORANGE = (255,165,0)

# Clock
clock = pygame.time.Clock()

#gane panel
info_panel = pygame.Rect(0,0,300,800)
game_panel = pygame.Rect(300,0,500,800)

#fonts
name = pygame.font.Font(None,50)
score = pygame.font.Font(None,35)

#play buttons
play_button = pygame.Rect(50,400,50,50)
reset_button = pygame.Rect(200,400,50,50)

#next block square
next_block = pygame.Rect(20,20,260,160)

#score
score = 0

#run game
running = True

while running:

    #screen background
    screen.fill(BLACK)

    #draw the panels
    pygame.draw.rect(screen,ORANGE,info_panel,10)
    pygame.draw.rect(screen,ORANGE,game_panel,10)

    tittle = name.render("BRICK BLOCK",True,WHITE)
    screen.blit(tittle,(50,600))


    pygame.display.update()

    clock.tick(60)


pygame.quit()