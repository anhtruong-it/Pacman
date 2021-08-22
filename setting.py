from pygame.math import Vector2 as vec
#screen setting
WIDTH, HEIGHT = 610, 670
FPS = 60
TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH- TOP_BOTTOM_BUFFER, HEIGHT- TOP_BOTTOM_BUFFER

ROWS = 28
COLS = 30
#color
BLACK = (0,0,0)
RED = (255, 0, 0)
GREY = (110, 110, 104)
WHITE = (255,255,255)
#font
START_TEXT_SIZE = 26
START_FONT = 'Bauhaus 93'

#image
START_ICON = "pacmanLogo.png"
#player setting
PLAYER_START_POSITION = vec(1,1)