import sys
from pathlib import Path
import pygame
from pygame.font import Font
from pygame.locals import *
import gruvbox

def center_horizontal(target, dest):
    x = dest.get_width() / 2 - target.get_width() / 2
    return x

class Menu:
    def __init__(self, menu_items, font):
        self.menu_items = menu_items
        self.font = font
        self.subsurfaces = [ ]
        self.height = 0
        self.width = 0
        self.cursor = self.font.render('> ', True, gruvbox.fg['red'])
        self.cursor_pos = 0

        # Populate subsurfaces array with surfaces for each menu item, and calculate
        # the dimensions of the master surface
        for i, item in enumerate(self.menu_items):
            self.subsurfaces.append(self.font.render(item, True, gruvbox.fg['fg']))
            if self.subsurfaces[i].get_width() + self.cursor.get_width() > self.width:
                self.width = self.subsurfaces[i].get_width() + self.cursor.get_width()
            self.height += self.subsurfaces[i].get_height()

        # Create a master surface to hold the entire menu w/ transparent background
        self._surface = pygame.Surface((self.width, self.height))
        self._surface.set_colorkey('#000000')

    @property
    def surface(self):
        # Wipe the surface clean for new frame
        self._surface.fill('#000000')

        # Blit menu item surfaces onto the master surface
        for i, subsurface in enumerate(self.subsurfaces):
            # If selected, draw the cursor
            if i == self.cursor_pos:
                self._surface.blit(self.cursor, (0, i*subsurface.get_height()))
            self._surface.blit(subsurface, (self.cursor.get_width(), i*subsurface.get_height()))

        return self._surface
    
    def cursor_up(self):
        if self.cursor_pos - 1 < 0:
            self.cursor_pos -= 1

    def cursor_down(self):
        if self.cursor_pos + 1 >= self.menu_items.length():
            self.cursor_pos += 1

def main_menu(display):
    TITLE = 'Kingdom'
    MENU_ITEMS = ['Continue', 'Load Game', 'New Game', 'Settings', 'Quit']
    LARGE = 64
    MEDIUM = 48
    SMALL = 24
    FONT_PATH = Path('assets/computer_modern_font/cmuntb.ttf')

    title_font = Font(FONT_PATH, LARGE)
    title_surface = title_font.render(TITLE, False, gruvbox.fg['fg'])

    menu_font = Font(FONT_PATH, MEDIUM)
    menu = Menu(MENU_ITEMS, menu_font)

    while True:
        display.fill(gruvbox.bg['bg0_h'])
        display.blit(title_surface, (center_horizontal(title_surface, display),0))
        display.blit(menu.surface, (center_horizontal(menu.surface, display),200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((800, 600), vsync=True)
    main_menu(display)
