import pygame
import time
from pygame.sprite import DirtySprite
from setting import *
vec = pygame.math.Vector2

class Player():
    def __init__(self, app ,pos) -> None:
        self.app = app
        self.grid_pos = pos
        self.Pclose = pygame.image.load(PACMAN_CLOSE)
        self.Pclose = pygame.transform.scale(self.Pclose, PACMAN_SCALE)
        self.Popen = pygame.image.load(PACMAN_OPEN)
        self.Popen = pygame.transform.scale(self.Popen, PACMAN_SCALE)
        self.pix_pos = vec(self.grid_pos.x * self.app.cell_w +6 , self.grid_pos.y*self.app.cell_h + 6) 
        self.direction = vec(1, 0)
        self.close = True
        self.state_close = time.time()

    def draw(self):
        if self.close == True:
            self.app.screen.blit(self.Pclose, self.pix_pos)
            pygame.draw.circle(self.app.screen, RED, self.pix_pos,2)
        else: 
            self.app.screen.blit(self.Popen, self.pix_pos)
            pygame.draw.circle(self.app.screen, RED, self.pix_pos,2)

    def change_state(self):
        if (time.time() - self.state_close) >= 0.2:
            self.close = not self.close
            self.state_close = time.time()

    def update(self):
        self.pix_pos += self.direction

    def moveRight(self):
        self.Pclose = pygame.transform.rotate(self.Pclose, -90)
        self.Popen = pygame.transform.rotate(self.Popen, -90)

    def moveLeft(self):
        self.Pclose = pygame.transform.rotate(self.Pclose, 90)
        self.Popen = pygame.transform.rotate(self.Popen, 90)

    def moveBack(self):
        self.Pclose = pygame.transform.rotate(self.Pclose, 180)
        self.Popen = pygame.transform.rotate(self.Popen,180)
    def move(self, direction):
        if self.direction.x == direction.y  and self.direction.y == direction.x*-1:
            self.moveRight()
        elif self.direction.x == direction.y*-1  and self.direction.y == direction.x:
            self.moveLeft()
        elif self.direction + direction == vec(0,0):
            self.moveBack()
        self.direction = direction


