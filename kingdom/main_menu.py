import sys
from pathlib import Path
import pygame
from pygame.font import Font
from pygame.locals import *
import gruvbox

def center_horizontal(target, dest):
    x = dest.get_width() / 2 - target.get_width() / 2
    return x

def main_menu(display):
    TITLE = 'Kingdom'
    MENU_ITEMS = ['Continue', 'Load Game', 'New Game', 'Settings', 'Quit']
    LARGE = 64
    MEDIUM = 48
    SMALL = 24
    FONT_PATH = Path('assets/computer_modern_font/cmuntb.ttf')

    title_font = Font(FONT_PATH, LARGE)
    title_surface = title_font.render(TITLE, False, gruvbox.fg['fg'])

    menu_item_font = Font(FONT_PATH, MEDIUM)
    item_surfaces = [ ]
    height = 0
    max_width = 0
    for i, item in enumerate(MENU_ITEMS):
        item_surfaces.append(menu_item_font.render(item, True, gruvbox.fg['fg']))
        if item_surfaces[i].get_width() > max_width:
            max_width = item_surfaces[i].get_width()
        height += item_surfaces[i].get_height()
    menu_surface = pygame.Surface((max_width, height))
    menu_surface.set_colorkey('#000000')
    for i, surface in enumerate(item_surfaces):
        menu_surface.blit(surface, (0, i*surface.get_height()))


    while True:
        display.fill(gruvbox.bg['bg0_h'])
        display.blit(title_surface, (center_horizontal(title_surface, display),0))
        display.blit(menu_surface, (center_horizontal(menu_surface, display),200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((800, 600), vsync=True)
    main_menu(display)
