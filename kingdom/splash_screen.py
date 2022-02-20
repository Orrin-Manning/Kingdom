import sys
import pygame
from pygame.locals import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600), RESIZABLE)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
