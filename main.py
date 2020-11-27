"""
Snake Game
by Your Favourite Student, even more than Josh (Josh kinda sucks), Isaac Aaron Kogan
Birthdate: 4/20/2004
"""

import os, random, sys, time
from modules.draw_game_board import draw_game_board
from modules.rounded_rectangles import rounded_rectangle
from modules.parse_time import parse_time
from modules.settings import *


# Removing any old end game screen files (cleaning up shop)
try: os.remove("resource_end_game_screen.png")
except FileNotFoundError: pass

# Main Process Loop (Allows for playing the game again when you die)

while True:

    # Start Menu Loop

    while run_start_menu:  # Boolean while loop for start menu

        # Handling Events

        for event in pygame.event.get():

            # IF THEY CLICK THE EXIT BUTTON
            if event.type == pygame.QUIT: pygame.quit(), sys.exit()  # Exit game

            # IF THEY CLICK THE SPACE BAR KEY
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: run_start_menu, run_game = False, True  # Start game

            # IF THEY CLICK THE MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()  # Getting mouse position

                # START BUTTON
                if (552 <= mouse[0] <= 1058) and (285 <= mouse[1] <= 495):
                    run_start_menu, run_game = False, True  # Start game

                # Difficulty Buttons

                # EASY DIFFICULTY
                if (170 <= mouse[0] <= 420) and (690 <= mouse[1] <= 782):
                    if difficulty == 'easy': dis.blit(checkmark_image, (mouse[0] - 30, mouse[1] - 50)), pygame.display.flip(), time.sleep(0.15)  # 'checkmark' image if it's already their difficulty
                    else:
                        difficulty = 'easy'  # Setting difficulty
                        difficulty_text_width, difficulty_text_height = scoreboard_font.size(difficulty.capitalize())  # Calculating difficulty text width, length
                        difficulty_colour, difficulty_offset = GREEN, ((SBRD_ITEM_WIDTH / 2) - (difficulty_text_width / 2))  # Setting difficulty-based colouring & text offsets
                        PPT, TILES, speed, snake_speed_limit, snake_speed_increase_interval, snake_speed_increase_amount, walls = 16, 40, 6, 15, 5, 1, 40  # Setting difficulty-based values

                # MEDIUM DIFFICULTY
                if (500 <= mouse[0] <= 750) and (690 <= mouse[1] <= 782):
                    if difficulty == 'medium': dis.blit(checkmark_image, (mouse[0] - 30, mouse[1] - 50)), pygame.display.flip(), time.sleep(0.15)  # 'checkmark' image if it's already their difficulty
                    else:
                        difficulty = 'medium'  # Setting difficulty
                        difficulty_text_width, difficulty_text_height = scoreboard_font.size(difficulty.capitalize())  # Calculating difficulty text width, length
                        difficulty_colour, difficulty_offset = YELLOW, ((SBRD_ITEM_WIDTH / 2) - (difficulty_text_width / 2))  # Setting difficulty-based colouring & text offsets
                        PPT, TILES, speed, snake_speed_limit, snake_speed_increase_interval, snake_speed_increase_amount, walls = 32, 20, 6, 10, 10, 1, 10  # Setting difficulty-based values

                # HARD DIFFICULTY
                if (820 <= mouse[0] <= 1070) and (690 <= mouse[1] <= 782):
                    if difficulty == 'hard': dis.blit(checkmark_image, (mouse[0] - 30, mouse[1] - 50)), pygame.display.flip(), time.sleep(0.15)  # 'checkmark' image if it's already their difficulty
                    else:
                        difficulty = 'hard'  # Setting difficulty
                        difficulty_text_width, difficulty_text_height = scoreboard_font.size(difficulty.capitalize())  # Calculating difficulty text width, length
                        difficulty_colour, difficulty_offset = RED, ((SBRD_ITEM_WIDTH / 2) - (difficulty_text_width / 2))  # Setting difficulty-based colouring & text offsets
                        PPT, TILES, speed, snake_speed_limit, snake_speed_increase_interval, snake_speed_increase_amount, walls = 64, 10, 5, 6, 50, 1, 4  # Setting difficulty-based values

        # Drawing Graphics

        # BACKGROUND
        dis.blit(gradient, (0, 0))  # Drawing the background gradient
        # GAME BOARD
        pygame.draw.rect(   # Game Board Border
            dis, GBRD_COLOUR_BORDER,
            (
                GBRD_START_X - GBRD_BORDER_THICKNESS, GBRD_START_Y - GBRD_BORDER_THICKNESS, PPT * TILES + 2 * GBRD_BORDER_THICKNESS,
                PPT * TILES + 2 * GBRD_BORDER_THICKNESS)
            )
        draw_game_board(PPT, TILES, GBRD_START_X, GBRD_START_Y)  # Drawing the game board

        # "ISAAC'S SNAKE GAME" TITLE
        rounded_rectangle(dis, (90, 20, 1070, 130), DARK_TURQUOISE, 0.2)  # Drawing the background rectangle
        dis.blit(title_font.render("Isaac's Snake Game", 1, WHITE), (235, 53))  # Blitting, rendering the text
        # SNAKE IMAGE
        dis.blit(snake_image, (95, 240))  # Blitting the snake image
        # "PRESS SPACE" IMAGE
        rounded_rectangle(dis, (500, 250, 600, 280), DARK_TURQUOISE)  # Spawning the background rectangle for the "Press Space" resource
        dis.blit(space_image, (550, 285))  # Drawing the "Press Space" resource
        # BACKGROUND FOR MODE SELECTION MODAL
        rounded_rectangle(dis, (90, 640, 1070, 200), (23, 110, 104))
        rounded_rectangle(dis, (100, 650, 1050, 180), GBRD_COLOUR_BORDER)

        # PUTTING A BACKGROUND AROUND THE DIFFICULTY CURRENTLY SELECTED
        if difficulty == 'easy': rounded_rectangle(dis, (160, 680, 270, 112), GREEN_DARK, 0.2)      # If Easy
        if difficulty == 'medium': rounded_rectangle(dis, (490, 680, 270, 112), YELLOW_DARK, 0.2)   # If Medium
        if difficulty == 'hard': rounded_rectangle(dis, (810, 680, 270, 112), RED_DARK, 0.2)        # If Hard

        # DIFFICULTY BUTTONS CREATION (DYNAMICALLY BASED ON WHETHER OR NOT THEY ARE MOUSING OVER IT)
        mouse = pygame.mouse.get_pos()  # Getting the mouse pos
        if ((170 <= mouse[0] <= 420) and (690 <= mouse[1] <= 782)) and difficulty != 'easy':        # If Easy
            rounded_rectangle(dis, (170, 690, 250, 92), GREEN_DARK, 0.2)                            # Change the button to dark green
            dis.blit(button_font.render("Easy", 1, WHITE_DARK), (240, 713))                         # Change the font to dark white
        else:
            rounded_rectangle(dis, (170, 690, 250, 92), GREEN, 0.2)                         # Otherwise Green
            dis.blit(button_font.render("Easy", 1, WHITE), (240, 713))                      # Otherwise White

        if ((500 <= mouse[0] <= 750) and (690 <= mouse[1] <= 782)) and difficulty != 'medium':      # If Medium
            rounded_rectangle(dis, (500, 690, 250, 92), YELLOW_DARK, 0.2)                           # Change the button to dark yellow
            dis.blit(button_font.render("Medium", 1, WHITE_DARK), (535, 713))                       # Change the font to dark white
        else:
            rounded_rectangle(dis, (500, 690, 250, 92), YELLOW, 0.2)                        # Otherwise Yellow
            dis.blit(button_font.render("Medium", 1, WHITE), (535, 713))                    # Otherwise White

        if ((820 <= mouse[0] <= 1070) and (690 <= mouse[1] <= 782)) and difficulty != 'hard':       # If Hard
            rounded_rectangle(dis, (820, 690, 250, 92), RED_DARK, 0.2)                              # Change the button to dark red
            dis.blit(button_font.render("Hard", 1, WHITE_DARK), (885, 713))                         # Change the font to dark white
        else:
            rounded_rectangle(dis, (820, 690, 250, 92), RED, 0.2)                           # Otherwise Red
            dis.blit(button_font.render("Hard", 1, WHITE), (885, 713))                      # Otherwise White

        pygame.display.flip()  # Updating the Display

        # Startup Parameters / Things that need to happen before the game starts

        if run_game:

            # Generating Walls, Food

            # FOOD GENERATION
            food_pos = GBRD_START_X + PPT * (random.randint(1, TILES - 1)), GBRD_START_Y + PPT * (random.randint(0, TILES - 1))

            # WALL GENERATION
            walls_pos, genned_walls = [], 0
            while genned_walls < walls:

                gen_wall = [GBRD_START_X + PPT * (random.randint(1, TILES - 1)), GBRD_START_Y + PPT * (random.randint(0, TILES - 1))]   # Generating a wall randomly
                if not (gen_wall[0] == food_pos[0] and gen_wall[1] == food_pos[1]) and not (gen_wall[0] <= GBRD_START_X + PPT * 3):     # Checking if it collides w/ food, the snake
                    walls_pos.append(gen_wall)  # Appending to successful wall gens
                    genned_walls += 1           # Adding to successful wall gens value

            # Setting Initial Values (Must be done here as they need to be reset every time the game starts, therefore can't be done in #settings

            # COUNTERS
            score = 0                                                                                   # Setting the initial score to 0
            food = 0                                                                                    # Setting the initial food to 0

            # TIMERS
            food_timer = time_per_food                                                                  # Resetting food timer
            timer_colour = GREEN                                                                        # Resetting initial food timer colour
            game_timer = 0                                                                              # Resetting game timer
            time_since_food = 0                                                                         # Resetting time-since-food timer

            # SNAKE
            snake_pos = [GBRD_START_X + PPT, GBRD_START_Y + PPT * (random.randint(1, TILES - 2))]       # Randomizing snake spawn
            snake_body = [[-100, -100], [-100, -100], [-100, -100]]                                     # Resetting initial snake location
            direction = '→'                                                                             # Resetting initial snake direction
            current_colour = SNAKE_START_RED_VALUE  # Resetting snake body colour

            # OTHER
            intro = None                                                                                # Resetting Intro Value
            high_score_constructor = ""                                                                 # Resetting high score constructor (for end game menu)
            high_scores = []                                                                            # Resetting high scores list (for end game menu)

    # Main Game Loop

    while run_game:

        # Intro Screen (Runs after 1 frame has been completed)

        if intro == "run":
            # COUNTDOWN SOUND
            pygame.mixer.Sound.play(countdown_sound)

            # 3
            dis.blit(countdown_font.render("3", 1, WHITE), (590, 180))
            pygame.display.flip(), time.sleep(0.6)

            # 2
            dis.blit(countdown_font.render("2", 1, WHITE), (590, 330))
            pygame.display.flip(), time.sleep(0.6)

            # 1
            dis.blit(countdown_font.render("1", 1, WHITE), (600, 480))
            pygame.display.flip(), time.sleep(0.6)

            # GAME MUSIC STARTS
            pygame.mixer.music.play(-1)

            # GO
            dis.blit(countdown_font.render("GO", 1, WHITE), (555, 630))
            pygame.display.flip(), time.sleep(0.6)

            # Preventing this from going off again
            intro = "null"

        # Handling Events

        for event in pygame.event.get():

            # IF THEY CLICK THE QUIT BUTTON
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()

            # IF THEY CLICK A KEY (DIRECTION HANDLING)
            if event.type == pygame.KEYDOWN:
                # Setting the direction, checking if it's equal to their negative direction and not allowing them to change if it is
                direction = '↑' if (event.key == ord('w') or event.key == pygame.K_UP) and direction != '↓' else direction
                direction = '←' if (event.key == ord('a') or event.key == pygame.K_LEFT) and direction != '→' else direction
                direction = '↓' if (event.key == ord('s') or event.key == pygame.K_DOWN) and direction != '↑' else direction
                direction = '→' if (event.key == ord('d') or event.key == pygame.K_RIGHT) and direction != '←' else direction

            # EVENT TIMERS
            if event.type == pygame.USEREVENT:
                if not food_timer < 0.01: food_timer -= 0.01  # Check if its < 0.01 for aesthetic purposes in the scoreboard
                time_since_food += 0.01
                game_timer += 0.01

        # Handling Snake Movement

        if direction == '↑': snake_pos[1] -= PPT
        if direction == '↓': snake_pos[1] += PPT
        if direction == '←': snake_pos[0] -= PPT
        if direction == '→': snake_pos[0] += PPT

        # Food Calculations

        # IF THE LOCATION OF A PIECE OF FOOD MATCHES THE LOCATION OF THE SNAKE
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            pygame.mixer.Sound.play(apple_eat_sound)  # Play the food eat sound

            # POWER-UP IF FOOD EATEN WITHIN 2 SECONDS
            if time_since_food < power_up_time:
                time_per_food += 1  # Increase the time per each food
                pygame.mixer.Sound.play(power_up_sound)  # Power up sound

            # ADDING TO SCORE, FOOD, RESETTING VALUES
            score, food, food_timer, time_since_food, timer_colour = (score_increase_amount + score), (food + 1), time_per_food, 0, GREEN
            print(f"Score: {score}")  # Score print debug (it was on the rubric, so it's here)

            # PREVENTING SCORE FROM EXCEEDING 99,999 FOR DISPLAY PURPOSES
            if len(str(score)) > 5: score = 99999
            if len(str(food)) > 5: food = 99999

            # INCREASING SPEED EVERY X ITEMS EATEN
            if speed <= snake_speed_limit and food % snake_speed_increase_interval == 0:
                speed += snake_speed_increase_amount  # Increase the speed
                pygame.mixer.Sound.play(speed_up_sound)  # Speed up sound

            # Spawning Food

            # SPAWNING NEW FOOD & VERIFYING FOOD ISN'T IN A WALL, REDRAWING UNTIL VALID
            while True:
                found, food_pos = False, (GBRD_START_X + PPT * (random.randint(1, TILES - 1)), GBRD_START_Y + PPT * (random.randint(1, TILES - 1)))  # Randomizing Spawn
                for w in walls_pos:
                    if food_pos[0] == w[0] and food_pos[1] == w[1]: found = True  # If the wall is in the snake
                if not found: break  # Breaking if it isn't in the snake's body

        # If the snake did NOT eat a piece of food, pop the snake body (THIS IS VERY IMPORTANT, IT'S WHAT CAUSES THE END OF THE SNAKE SEGMENTS TO DISAPPEAR)
        else:
            snake_body.pop()

        # Collision Checks (Must be done pre-graphic rendering to prevent the snake from 'exiting' the map on the screen if it goes out of bounds, hits a well, etc.)

        # IF THE SNAKE HITS A WALL CHECK
        found_snake_in_wall = False
        for w in walls_pos:
            if snake_pos[0] == w[0] and snake_pos[1] == w[1]: found_snake_in_wall = True  # If it hits wall

        # IF THE SNAKE GOES OUT OF BOUNDS CHECK
        snake_out_of_bounds = False
        if snake_pos[0] < GBRD_START_X or snake_pos[0] > GBRD_START_X + (PPT * TILES) - 1:  snake_out_of_bounds = True  # X Boundary
        if snake_pos[1] < GBRD_START_Y or snake_pos[1] > GBRD_START_Y + (PPT * TILES) - 1:  snake_out_of_bounds = True  # Y Boundary

        # IF EITHER HAPPEN, TAKE A SCREENSHOT NOW (FOR THE END GAME, SINCE THEY ARE ABOUT TO DIE)
        if found_snake_in_wall or snake_out_of_bounds:
            pygame.image.save(dis, "./resources/resource_end_game_screen.png")  # Save screenshot image for death screen

        # Drawing Graphics to the Screen

        # IF THE SNAKE DIDN'T COLLIDE WITH A WALL OR GO OUT OF BOUNDS
        if not found_snake_in_wall and not snake_out_of_bounds:

            # Display & Game Board

            # DRAWING THE DISPLAY, GAME BOARD
            dis.blit(gradient, (0, 0))  # Drawing the background

            pygame.draw.rect(  # Drawing the game board border
                dis, GBRD_COLOUR_BORDER,
                (
                    GBRD_START_X - GBRD_BORDER_THICKNESS, GBRD_START_Y - GBRD_BORDER_THICKNESS, PPT * TILES + 2 * GBRD_BORDER_THICKNESS,
                    PPT * TILES + 2 * GBRD_BORDER_THICKNESS)
            )

            draw_game_board(PPT, TILES, GBRD_START_X, GBRD_START_Y)  # Drawing the game board

            # Scoreboards

            # DRAWING THE SCOREBOARD ITEM BACKGROUNDS
            rounded_rectangle(dis, (sbrd_item_1_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), timer_colour)          # Item 1
            rounded_rectangle(dis, (sbrd_item_2_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), difficulty_colour)     # Item 2
            rounded_rectangle(dis, (sbrd_item_3_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), GBRD_COLOUR_DARK)      # Item 3
            rounded_rectangle(dis, (sbrd_item_4_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), GBRD_COLOUR_DARK)      # Item 4

            # TIMER SCOREBOARD
            # SETTING THE COLOUR
            if food_timer < (5 / 10) * time_per_food:  # 10
                timer_colour = YELLOW
                if food_timer < (1 / 3) * time_per_food:  # 7
                    timer_colour = ORANGE
                    if food_timer < (1 / 6) * time_per_food:  # 3
                        timer_colour = RED
            # SETTING THE ITEM OFFSET (PSEUDO-CENTERING)
            if food_timer >= 1000: timer_offset = -24       # -24 px
            elif food_timer >= 100: timer_offset = -12      # -12 px
            elif food_timer <= 10: timer_offset = 10        # +10 px
            else: timer_offset = 0                          # +-0 px
            dis.blit(timer_image, (sbrd_item_1_pos_x + 40 + timer_offset, sbrd_text_y - 7))  # Drawing timer image
            dis.blit(scoreboard_font.render(f"{round(food_timer, 1)}s", 1, WHITE), (sbrd_coord_x + 95 + timer_offset, sbrd_text_y))  # Drawing timer text

            # DIFFICULTY SCOREBOARD
            dis.blit(scoreboard_font.render(difficulty.capitalize(), 1, WHITE), (sbrd_item_2_pos_x + difficulty_offset, sbrd_text_y))  # Drawing difficulty

            # SCORE SCOREBOARD
            score_text = f"Score: {score}"  # Calculating 'score' string
            score_text_width, score_text_height = scoreboard_font.size(score_text)  # Calculating text w/h
            score_text_offset = (SBRD_ITEM_WIDTH - score_text_width) / 2  # Calculating offset based on w/h for centering
            dis.blit(scoreboard_font.render(score_text, 1, WHITE), (sbrd_item_3_pos_x + score_text_offset, sbrd_text_y))  # Drawing text

            # FOOD SCOREBOARD
            food_text = f"x {food}"  # Calculating 'food' string
            food_text_width, food_text_height = scoreboard_font.size(food_text)  # Calculating text w/h
            food_text_offset = (SBRD_ITEM_WIDTH - food_text_width - SBRD_ITEM_4_FOOD_SIZE) / 2  # Calculating offset based on w/h for centering
            pygame.draw.rect(dis, WHITE, pygame.Rect(sbrd_item_4_pos_x + food_text_offset, sbrd_text_y, SBRD_ITEM_4_FOOD_SIZE, SBRD_ITEM_4_FOOD_SIZE))  # Drawing the Symbol
            dis.blit(scoreboard_font.render(food_text, 1, WHITE), (sbrd_item_4_pos_x + 40 + food_text_offset, sbrd_text_y))  # Drawing text

            # Drawing the Snake

            snake_body.insert(0, list(snake_pos))  # Snake Values Constructor

            # GENERATING SNAKE BODY COLOURS
            flip = False  # Setting the flip-flop
            for pos in snake_body:  # Iterating through the snake
                if flip:  # Subtracting red value if "Flip = True"
                    current_colour, flip = (current_colour + snake_colour_interval, flip) if current_colour + snake_colour_interval < 225 else (current_colour - snake_colour_interval, False)
                else:  # Adding red value if "Flip = False"
                    current_colour, flip = (current_colour - snake_colour_interval, flip) if current_colour - snake_colour_interval > 81 else (current_colour + snake_colour_interval, True)

            # DRAWING THE SNAKE
                pygame.draw.rect(dis, (current_colour, 45, 180), pygame.Rect(pos[0], pos[1], PPT, PPT))  # Drawing the Segment
            pygame.draw.rect(dis, SNAKE_COLOUR_HEAD, pygame.Rect(snake_pos[0], snake_pos[1], PPT, PPT))  # Overwriting the Head

            # DRAWING THE FOOD
            pygame.draw.rect(dis, WHITE, pygame.Rect(food_pos[0], food_pos[1], PPT, PPT))  # Draw Food

            # DRAWING THE WALLS
            for w in walls_pos:  # For every wall
                pygame.draw.rect(dis, DARK_TURQUOISE, pygame.Rect(w[0], w[1], PPT, PPT))  # Draw Wall item

        # Checking Bounds (End-Game Conditions)

        # IF THE SNAKE EXITS THE MAP
        if snake_out_of_bounds:
            run_game = False                                                                    # Stop looping the game
            pygame.mixer.Sound.play(wall_crash_sound)                                           # Play crash sound

        # IF THE SNAKE CUTS INTO ITSELF
        for segment in snake_body[1:]:                                                          # For each segment check if it cuts in
            if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:  run_game = False     # If the segment overlaps with another, stop looping the game

        # IF THE SCORE, FOOD >= 99,999 (SCOREBOARD LIMIT, GAME WIN CLAUSE)
        if score >= 99999 or food >= 99999:                                                     # If score, food >= 99,999
            if score >= 99999: score = 99999
            if food >= 99999: food = 99999
            run_game = False                                                                    # End the game

        # IF THEY RUN OUT OF TIME
        if food_timer < 0.01: run_game = False                                                  # If out of time, end the game

        # IF THE SNAKE HITS A WALL/OBSTACLE
        if found_snake_in_wall:                                                                 # If the snake hits a wall
            pygame.mixer.Sound.play(wall_crash_sound)                                           # Play crash sound
            run_game = False                                                                    # End the game

        # After 1 frame, start the Intro

        if intro is None:
            intro = "run"  # "run" is the parameter the 'intro' if statement earlier in the code looks for to run the intro

        # Final Display Updates

        pygame.display.flip()                       # Update Text
        fps_controller.tick(speed)                  # Update FPS Tick Speed
        if not run_game: run_end_menu = True        # If the game is over, start the end menu

    # End Menu Loop

    if run_end_menu:

        # Startup Parameters / Things that need to happen before the end menu runs

        if not found_snake_in_wall and not snake_out_of_bounds: pygame.image.save(dis, "./resources/resource_end_game_screen.png")  # Save a final screenshot of the board if it hasn't already
        pygame.mixer.music.stop(), pygame.mixer.Sound.play(game_over_sound)  # Play the end game sound, stop the music

        # Create High Score

        # GRAB RAW DATA
        file = open("resources/resource_high_score.txt", "r")    # Open the file in read mode
        raw_high_scores = file.read()                             # Grab the raw data
        file.close()                                              # Close the file

        # PARSE DATA INTO USABLE LIST
        for char in raw_high_scores:  # Iterating through each char in the file
            if not char == ":": high_score_constructor += char  # Splitting at every ":" otherwise adding to the constructor
            else:
                high_scores.append(high_score_constructor)  # Adding to high scores list
                high_score_constructor = ""  # Resetting constructor

        # GRAB THE APPLICABLE HIGH SCORE FROM THE LIST BASED ON YOUR MODE (EASY, MEDIUM, HARD)

        if difficulty == 'easy': hs_range, high_score = 0, high_scores[hs_range]
        elif difficulty == 'medium': hs_range, high_score = 1, high_scores[hs_range]
        elif difficulty == 'hard': hs_range, high_score = 2, high_scores[hs_range]

        # CHECK IF YOUR SCORE EXCEEDS THE HIGH SCORE & WRITE A NEW ONE IF IT DOES
        if int(high_score) < score:  # If it exceeds it
            high_scores[hs_range] = score  # Change the the high score locally (for the scoreboard display later)

            # CONVERTING BACK TO RAW DATA
            for idx, i in enumerate(high_scores):  # Turn the high scores intro strings so they can be joined into a string from a list (can't join integers)
                high_scores[idx] = str(i)

            # WRITING TO FILE
            file = open("resources/resource_high_score.txt", "w")      # Open the file in write mode
            file.write(":".join(high_scores) + ":")                     # Join the list into raw data, write it to the file
            file.close()                                                # Close the file

            new_or_not = "NEW!"                                         # Tell the scoreboard you got a new high score
        else:
            new_or_not = ""                                             # Display nothing in that spot if you didn't get a new high score

    # End Menu Loop

    while run_end_menu:

        # Handling Events

        for event in pygame.event.get():

            # IF THEY CLICK THE QUIT BUTTON
            if event.type == pygame.QUIT:
                os.remove("./resources/resource_end_game_screen.png"), pygame.quit(), sys.exit()  # Remove the end-game screenshot (to be used in the end-game menu)

            # IF THEY CLICK A MOUSE BUTTON
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()  # Get the mouse pos

                # IF THEY CLICK PLAY AGAIN SCREEN BUTTON, PLAY AGAIN
                if (40 <= mouse[0] <= 260) and (684 <= mouse[1] <= 774): run_end_menu, run_start_menu = False, True

            # IF THEY CLICK THE SPACE BAR, PLAY AGAIN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: run_end_menu, run_start_menu = False, True

        # End Screen Graphics

        # DRAW MAIN BACKING (THE OLD GAME DISPLAY) (We cheat, and use that image, it's easier and more reliable)
        dis.blit(pygame.image.load('./resources/resource_end_game_screen.png'), (0, 0))  # Load and draw background image

        # DRAW THE GAME OVER TEXT/BACKGROUND RECTANGLE
        rounded_rectangle(dis, (20, 20, 1220, 130), DARK_TURQUOISE, 0.2)  # Draw game over backing
        dis.blit(title_font.render("Game Over", 1, WHITE), (415, 50))  # Draw game over text

        # End Screen Scoreboard Graphics

        # DRAW THE END SCREEN SCOREBOARD RECTANGLE
        rounded_rectangle(dis, (20, 200, 260, 600), TURQUOISE, 0.2)  # Draw rounded rectangle for end screen scoreboard

        # HIGH SCORE DISPLAY
        dis.blit(end_screen_font.render("HIGH SCORE", 1, WHITE), (55, 230))  # Draw 'HIGH SCORE' header
        dis.blit(scoreboard_font.render(f"{high_scores[hs_range]} {new_or_not}", 1, WHITE_DARK), (55, 280))  # Draw 'HIGH SCORE' value

        # YOUR SCORE DISPLAY
        dis.blit(end_screen_font.render("YOUR SCORE", 1, WHITE), (55, 350))  # Draw 'YOUR SCORE' header
        dis.blit(scoreboard_font.render(f"{score}", 1, WHITE_DARK), (55, 400))  # Draw 'YOUR SCORE' value

        # FOOD EATEN DISPLAY
        dis.blit(end_screen_font.render("FOOD EATEN", 1, WHITE), (55, 460))  # Drawing 'FOOD EATEN' header
        pygame.draw.rect(dis, WHITE_DARK, pygame.Rect(55, 510, SBRD_ITEM_4_FOOD_SIZE, SBRD_ITEM_4_FOOD_SIZE))  # Drawing Food Symbol
        dis.blit(scoreboard_font.render(f"x {food}", 1, WHITE_DARK), (95, 510))  # Drawing 'FOOD EATEN' value

        # GAME TIME DISPLAY
        dis.blit(end_screen_font.render("GAME TIME", 1, WHITE), (55, 580))  # Drawing 'GAME TIME' header
        dis.blit(scoreboard_font.render(f"{parse_time(game_timer)}", 1, WHITE_DARK), (55, 630))  # Drawing  'GAME TIME' value

        # REPLAY BUTTON (ON SCOREBOARD BECAUSE IT LOOKS GOOD THERE)
        dis.blit(replay_image, (39, 685))  # Drawing the replay button
        dis.blit(snake_image, (800, 310))  # Drawing the snake image

        # Update the display

        pygame.display.flip()  # Flipping/Updating the display
