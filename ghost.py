import pygame
import random
import time

from pygame.constants import SHOWN
from setting import *

vec = pygame.math.Vector2

class Ghost:
    def __init__ (self, app, pos, ghost_character):
        self.app = app
        self.id = ghost_character["id"]
        self.first_pic = pygame.image.load(ghost_character["firstPic"])
        self.first_pic = pygame.transform.scale(self.first_pic, GHOST_SCALE)
        self.second_pic = pygame.image.load(ghost_character["secondPic"])
        self.second_pic = pygame.transform.scale(self.second_pic, GHOST_SCALE)
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.change_pic = True
        self.time_change = time.time()

    def change_state(self):
        if time.time() - self.time_change >= 0.1 :
            self.change_pic = not self.change_pic
            self.time_change = time.time()
        
    def draw (self):
        ghost = vec(self.pix_pos.x - self.app.cell_w//2 , self.pix_pos.y-self.app.cell_h//2)
        if self.change_pic:
            self.app.screen.blit(self.first_pic, ghost)
        else:
            self.app.screen.blit(self.second_pic, ghost)

    def update(self):
        pass

    def get_pix_pos(self):
        return vec((self.grid_pos[0]*self.app.cell_w + 0.5*self.app.cell_w)+TOP_BOTTOM_BUFFER//2,
                   (self.grid_pos[1]*self.app.cell_h + 0.5*self.app.cell_h)+TOP_BOTTOM_BUFFER//2)
