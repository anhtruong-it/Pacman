import sys
import pygame
from player import *
from setting import *

pygame.init()
vec = pygame.math.Vector2
class App :
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'
        self.score = 0
        self.cell_h = MAZE_HEIGHT //COLS
        self.cell_w = MAZE_WIDTH //ROWS
        self.player = Player(self,PLAYER_START_POSITION)
        self.load()
    def run(self):
        while self.running :
            if self.state == 'intro':
                self.start_event()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_event()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
##################### HELP FUNCTION ################################33
    def draw_text(self, word,screen,pos, size, color, font_name, center = False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(word, False, color)
        text_size = text.get_size()
        if center:
            pos[0] = pos[0] - text_size[0] //2
            pos[1] = pos[1] - text_size[1] //2
        screen.blit(text,pos)
    
    def load(self):
        self.icon = pygame.image.load(START_ICON)
        background = pygame.image.load('maze.png')
        self.background = pygame.transform.scale(background,(MAZE_WIDTH, MAZE_HEIGHT))

    def darw_grid(self):
        for x in range(WIDTH//self.cell_w):
            pygame.draw.line(self.background, GREY , (x*self.cell_w, 0),(x*self.cell_w, HEIGHT))
        for y in range(HEIGHT//self.cell_h):
            pygame.draw.line(self.background, GREY , (0, y * self.cell_h),(WIDTH, y*self.cell_h))
##################### START FUNCTION ################################33

    def start_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = 'playing'
                print("Space press")

    def start_update(self):
        pass
    def start_draw(self):
        self.screen.fill (BLACK)
        icon = pygame.transform.scale(self.icon, (100,100))
        self.screen.blit(icon,[WIDTH//2 -50, HEIGHT//2 -150])

        self.draw_text("PUSH SPACE BAR",self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (170,132,58) , START_FONT, center = True)
        self.draw_text("1 Player Only",self.screen, [WIDTH//2, HEIGHT//2 + 50], START_TEXT_SIZE, (25, 73, 215) , START_FONT, center = True)
        self.draw_text("HIGHEST SCORE: {}".format(self.score),self.screen, [4, 0], START_TEXT_SIZE, (255,255,255) , START_FONT)
        pygame.display.update()

##################### Playing FUNCTION ################################33
    def playing_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            

    def playing_update(self):
        pass
    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit (self.background,(TOP_BOTTOM_BUFFER//2, TOP_BOTTOM_BUFFER//2))
        self.darw_grid()
        self.draw_text("CURRENT SCORE: {}".format(0),self.screen, [50, 5], 18, WHITE , START_FONT)
        self.draw_text("HIGH SCORE: {}".format(0),self.screen, [WIDTH//2, 5], 18, WHITE , START_FONT)
        pygame.display.update()