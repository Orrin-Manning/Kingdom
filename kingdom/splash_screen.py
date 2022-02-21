import sys
from pathlib import Path
import pygame
from pygame.locals import *
from pygame.font import Font
import gruvbox

def splash_screen(display):
    dev_name = 'Snake Oil Software'
    dev_font_path = Path('assets/computer_modern_font/cmuntx.ttf')

    dev_font = Font(dev_font_path, 36)
    print(dev_font)

    dev_surface = dev_font.render(dev_name, True, gruvbox.fg['fg'])

    # Draw Screen
    display.blit(dev_surface, (0,0))

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((800, 600), RESIZABLE)
    splash_screen(display)
