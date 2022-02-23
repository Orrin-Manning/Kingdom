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

# def rise_and_freeze():

def splash_screen(display):
    dev_name = 'Snake Oil Software'
    dev_font_path = Path('assets/durango-western-eroded/Durango Western Eroded Demo.otf')

    dev_font = Font(dev_font_path, 64)

    dev_surface = dev_font.render(dev_name, False, gruvbox.fg['yellow'])
    
    initial_time = pygame.time.get_ticks()
    # Loop terminates 5 seconds after initial_time is set
    while pygame.time.get_ticks() - initial_time < 5000:
        center_pos = get_center(dev_surface.get_size(), display.get_size())

        display.fill(gruvbox.bg['bg0'])
        display.blit(dev_surface, center_pos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

# For testing, if script is run standalone, perform basic initialization
# of display to preview behavior of the splash screen
if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((800, 600), RESIZABLE)
    splash_screen(display)
