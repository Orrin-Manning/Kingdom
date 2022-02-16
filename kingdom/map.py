import pygame
from pygame import Surface
from pygame.locals import *
from cell import Cell
from cursor import Cursor
import gruvbox

class Map:
    def __init__(self, width=6, height=6):
        self.width = width
        self.height = height
        self.cell_array = [[Cell() for x in range(width)] for y in range(height)]

    def set_width(self, width):
        if width <= 0:
            raise ValueError('board width must be positive')
        self._width = width

    def get_width(self):
        return self._width

    def set_height(self, height):
        if height <= 0:
            raise ValueError('board height must be positive')
        self._height = height

    def get_height(self):
        return self._height

    def render(self):
        font = 'firacodevf'
        font_size = 24
        font_path = pygame.font.match_font(font)
        character_printer = pygame.font.Font(font_path, font_size)
        character_size = character_printer.size(' ')

        surface = Surface((self._width * character_size[0], self._height * character_size[1]))
        for y in range(self._height):
            for x in range(self._width):
                character_surface = character_printer.render(str(self.cell_array[y][x]), True, gruvbox.fg['green'], gruvbox.bg['bg'])
                surface.blit(character_surface, (x * character_size[0], y * character_size[1]))

        return surface

    width = property(fget=get_width, fset=set_width)
    height = property(fget=get_height, fset=set_height)

    def __str__(self):
        map = ''
        for y in range(self.height):
            for x in range(self.width):
                map = map + '.'
            map = map + '\n'
        return map
