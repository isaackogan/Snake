import pygame

# Loading Display

pygame.init()                                                   # Initializing PyGame

FRAME_SIZE_X = 1260                                             # Frame Size (X-Value)
FRAME_SIZE_Y = 900                                              # Frame Size (Y-Value)
dis = pygame.display.set_mode((FRAME_SIZE_X, FRAME_SIZE_Y))     # Setting the Display

# Setting Colours

BLACK = pygame.Color(0, 0, 0)                       # Black
ORANGE = pygame.Color(240, 172, 46)                 # Orange

WHITE = pygame.Color(255, 255, 255)                 # White
WHITE_DARK = pygame.Color(224, 224, 224)            # Dark White

TURQUOISE = pygame.Color(45, 189, 181)              # Turquoise
DARK_TURQUOISE = pygame.Color(23, 110, 104)         # Dark Turquoise

GREEN = pygame.Color(36, 214, 105)                  # Green
GREEN_DARK = pygame.Color(30, 176, 87)              # Dark Green

YELLOW = pygame.Color(217, 205, 37)                 # Yellow
YELLOW_DARK = pygame.Color(176, 166, 30)            # Dark Yellow

RED = pygame.Color(171, 38, 17)                     # Red
RED_DARK = pygame.Color(138, 31, 14)                # Dark Red

GBRD_COLOUR_LIGHT = pygame.Color(48, 207, 199)      # Game Board "Light" Checker Colour
GBRD_COLOUR_DARK = pygame.Color(50, 219, 210)       # Game Board "Dark" Checker Colour
GBRD_COLOUR_BORDER = pygame.Color(34, 143, 137)     # Game Board Border Colour

SNAKE_COLOUR_HEAD = pygame.Color(46, 9, 82)         # Snake Head Colour
SNAKE_START_RED_VALUE = 72                          # Initial "RED" RGB Value for the snake body

# Loading Resources

gradient = pygame.transform.scale(pygame.image.load('resource_gradient.png'), (FRAME_SIZE_X, FRAME_SIZE_Y))     # Loading Background Image
snake_image = pygame.transform.scale(pygame.image.load('resource_snake_logo.png'), (325, 325))                  # Loading Snake Image
checkmark_image = pygame.transform.scale(pygame.image.load('resource_checkmark.png'), (64, 64))                 # Loading checkmark Image
space_image = pygame.transform.scale(pygame.image.load('resource_press_space.png'), (509, 209))                 # Loading "SPACE TO START" image
timer_image = pygame.transform.scale(pygame.image.load('resource_timer.png'), (44, 44))                         # Loading the timer image
replay_image = pygame.transform.scale(pygame.image.load('resource_replay.png'), (220, 90))

title_font = pygame.font.SysFont('Franklin Gothic', 110)                                                        # Loading Title Font
countdown_font = pygame.font.SysFont('Impact', 150)                                                             # Loading Title Font
button_font = pygame.font.SysFont('Franklin Gothic', 70)                                                        # Loading Button Font
scoreboard_font = pygame.font.SysFont('Lucidia Console', 50)                                                    # Loading Scoreboard Font
end_screen_font = pygame.font.SysFont('Impact', 40)
pygame.display.set_caption("Isaac's Snake Game (2020)"), pygame.display.set_icon(snake_image)                   # Setting the caption & Icon

pygame.mixer.music.load('resource_sound_background_music.mp3')
pygame.mixer.music.set_volume(0.4)

wall_crash_sound = pygame.mixer.Sound("resource_sound_wall_crash.wav")
game_over_sound = pygame.mixer.Sound("resource_sound_game_over.wav")
power_up_sound = pygame.mixer.Sound("resource_sound_power_up.wav")
speed_up_sound = pygame.mixer.Sound('resource_sound_speed_up.wav')
apple_eat_sound = pygame.mixer.Sound("resource_sound_apple_eat.wav")
countdown_sound = pygame.mixer.Sound("resource_sound_321_go.wav")

# Snake Settings

snake_colour_interval = 15                                                                      # Setting the colour change interval (what the red will be changed by)
snake_colour = SNAKE_COLOUR_HEAD                                                                # Setting the initial snake colour

# Game Board Settings

PPT = 16                                                                                        # Setting the "pixels per tile" value
TILES = 40                                                                                      # Setting the default "tiles per game board" value

GBRD_START_X = FRAME_SIZE_X // 2 - (PPT * TILES // 2)                                           # Calculating the game board's start position (centering it on the screen)
GBRD_START_Y = 180                                                                              # Setting the Y position of the game board

GBRD_BORDER_THICKNESS = 10                                                                      # Setting the border thickness of the game board

# Scoreboard Settings

SBRD_ITEM_WIDTH = 230                                                                           # Setting the width of each scoreboard item
SBRD_ITEM_HEIGHT = 72                                                                           # Setting the height of each scoreboard item
sbrd_item_spacer = 80                                                                           # Setting the space between each scoreboard item

sbrd_coord_x = 50                                                                               # Setting the coordinate of the first scoreboard item
sbrd_coord_y = (GBRD_START_Y / 2) - (SBRD_ITEM_HEIGHT / 2) - (GBRD_BORDER_THICKNESS / 2)        # centering the scoreboard's Y location between top of screen & top of gbrd border

sbrd_text_y = sbrd_coord_y + 20                                                                 # Setting the offset for 'text' items in the scoreboard (centering w/in rectangle)

sbrd_item_1_pos_x = (sbrd_coord_x + SBRD_ITEM_WIDTH * 0) + sbrd_item_spacer * 0                 # Setting the X position offset for Item 1 from the first scoreboard item
sbrd_item_2_pos_x = (sbrd_coord_x + SBRD_ITEM_WIDTH * 1) + sbrd_item_spacer * 1                 # Setting the X position offset for Item 2 from the first scoreboard item
sbrd_item_3_pos_x = (sbrd_coord_x + SBRD_ITEM_WIDTH * 2) + sbrd_item_spacer * 2                 # Setting the X position offset for Item 3 from the first scoreboard item
sbrd_item_4_pos_x = (sbrd_coord_x + SBRD_ITEM_WIDTH * 3) + sbrd_item_spacer * 3                 # Setting the X position offset for Item 4 from the first scoreboard item

SBRD_ITEM_4_FOOD_SIZE = 32                                                                      # Setting the size of the food icon in the scoreboard

# Food Settings

food_timer = 20                                                                                 # Setting the initial food timer value
time_per_food = food_timer                                                                      # Assigning a variable to keep track of the initial value
score_increase_amount = 20                                                                   # Assigning the score increase per food eaten

# Initial Values

direction = '→'                                                                                 # Setting the initial snake direction
change_to = direction                                                                           # Setting the initial direction change to the initial direction

score = 0                                                                                       # Setting the initial score to 0
food = 0                                                                                        # Setting the initial food to 0
game_timer = 0                                                                                  # Setting the initial game time to 0

timer_colour = GREEN                                                                            # Setting the initial timer colour
current_colour = SNAKE_START_RED_VALUE                                                          # Setting the initial snake colour

run_start_menu = True                                                                           # Running the start menu loop on program launch
run_game = False                                                                                # Setting the initial value for the game run loop
run_end_menu = False                                                                            # Setting the initial value for the end menu loop
out_of_bounds = False                                                                           # Setting the start value to FALSE for the snake being out of bounds

fps_controller = pygame.time.Clock()                                                            # Setting the initial clock
pygame.time.set_timer(pygame.USEREVENT, 10)                                                     # Initializing the timer

difficulty = 'medium'                                                                           # Setting the default difficulty
