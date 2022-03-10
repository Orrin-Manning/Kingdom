import pygame
from pygame.locals import *
import gruvbox

class Cursor:
    symbol = 'X'
    fg_color = gruvbox.fg['yellow']
    bg_color = gruvbox.bg['bg']

    def __init__(self, position=(0,0)):
        self.position = position

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def get_surface(self, font, fontsize):
        renderer = pygame.font.Font(font, fontsize)
        surface = renderer.render(symbol, True, fg_color, bg_color)
        return surface

    position = property(get_position, set_position)
