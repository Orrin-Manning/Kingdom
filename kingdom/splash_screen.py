import sys
from pathlib import Path
import pygame
from pygame.locals import *
from pygame.font import Font
import gruvbox

# Takes a target surface and a destination surface, returns a position
# that allows the target to be centered within the destination
def get_center(target_size, dest_size):
    x_pos= dest_size[0] / 2 - target_size[0] / 2
    y_pos= dest_size[1] / 2 - target_size[1] / 2
    position = (x_pos, y_pos)
    return position

def rise_and_freeze(t, dest, display_size):
    rise_t = 2000
    distance = display_size[1] - dest[1]
    if t < rise_t:
        position = (dest[0], display_size[1] - (t/rise_t)*distance)
    else:
        position = dest
    return position

# Main logic for splash screen
def splash_screen(display):
    FPS = 60
    frame_per_sec = pygame.time.Clock()

    dev_name = 'Snake Oil Software'
    dev_font_path = Path('assets/durango-western-eroded/Durango Western Eroded Demo.otf')

    dev_font = Font(dev_font_path, 64)

    dev_surface = dev_font.render(dev_name, False, gruvbox.fg['yellow'])
    center_pos = get_center(dev_surface.get_size(), display.get_size())
    
    # Loop terminates 5 seconds after initial_time is set
    initial_time = pygame.time.get_ticks()
    while (t := pygame.time.get_ticks() - initial_time) < 5000:
        # Calculate position of logo based on time
        dev_pos = rise_and_freeze(t, center_pos, display.get_size())

        # Wipe screen and print logo at new position in the frame
        display.fill(gruvbox.bg['bg0'])
        display.blit(dev_surface, dev_pos)
        pygame.display.update()

        # Handle manual close of the window
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        frame_per_sec.tick(FPS)

# For testing, if script is run standalone, perform basic initialization
# of display to preview behavior of the splash screen
if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((800, 600), vsync=True)
    splash_screen(display)
