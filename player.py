import pygame
from setting import *
vec = pygame.math.Vector2

class Player():
    def __init__(self, app ,pos) -> None:
        self.app = app
        self.grid_pos = pos
        self.pix_pos = vec(self.grid_pos.x * self.app.cell_w, self.grid_pos.y*self.app.cell_h)

