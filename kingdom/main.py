import sys
import pygame
from pygame.locals import *
from map import Map

pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()

screen = pygame.display.set_mode((1280,720))

map = Map(12, 12)

# Main game loop
while True:
    # Create surface of the game world
    map_surface = map.render()
    screen.blit(map_surface, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)
