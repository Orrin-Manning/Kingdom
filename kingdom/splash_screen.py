import sys
from pathlib import Path
import pygame
from pygame.locals import *
from pygame.font import Font
import gruvbox

# Takes a target surface and a destination surface, and returns a position
# that allows the target to be center within the destination
def get_center(target_size, dest_size):
    x_pos= dest_size[0] / 2 - target_size[0] / 2
    y_pos= dest_size[1] / 2 - target_size[1] / 2
    position = (x_pos, y_pos)
    return position

def splash_screen(display):
    dev_name = 'Snake Oil Software'
    dev_font_path = Path('assets/computer_modern_font/cmuntx.ttf')

    dev_font = Font(dev_font_path, 36)
    print(dev_font)

    dev_surface = dev_font.render(dev_name, True, gruvbox.fg['fg'])
    
    center_pos = get_center(dev_surface.get_size(), display.get_size())

    # Draw Screen
    display.blit(dev_surface, center_pos)

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
