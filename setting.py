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
YELLOW = (255,255,0)

#font
START_TEXT_SIZE = 26
START_FONT = 'Bauhaus 93'

#image
START_ICON = "pacmanLogo.png"
#player setting
PLAYER_START_POSITION = vec(1,1)

# The year and course code
COURSE_YEAR = "2021"
# Students:
STUDENT_SIZE = 20
STUDENT_FRONT = "Cooper Std"
STUDENTS = [("PHUC THIEN VUONG", "S5193954","2805ICT"),
("ANH TRUONG NGUYEN", "S5168384","2805ICT"),
("HIEN DAT CHU", "S5223891","3815ICT")
]

#Button setting
BUTTON_W = 150
BUTTON_H = 80

BUTTON_WORD_SIZE = 30
BUTTON_WORD_FONT = "Bauhaus 93"