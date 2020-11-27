"""
Snake Game
by Your Favourite Student, even more than Josh (Josh kinda sucks), Isaac Aaron Kogan
Birthdate: 4/20/2004
"""

import os
import random
import sys
import time

from modules.draw_game_board import draw_game_board
from modules.rounded_rectangles import rounded_rectangle
from modules.settings import *
from modules.parse_time import parse_time

try:
    os.remove("resource_end_game_screen.png")
except FileNotFoundError:
    pass

while True:
    while run_start_menu:

        for event in pygame.event.get():

            # If they click the quit button
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if (170 <= mouse[0] <= 420) and (690 <= mouse[1] <= 782):
                    if difficulty == 'easy':
                        dis.blit(checkmark_image, (mouse[0] - 30, mouse[1] - 50))
                        pygame.display.flip(), time.sleep(0.15)
                    else:
                        difficulty = 'easy'
                if (500 <= mouse[0] <= 750) and (690 <= mouse[1] <= 782):
                    if difficulty == 'medium':
                        dis.blit(checkmark_image, (mouse[0] - 30, mouse[1] - 50))
                        pygame.display.flip(), time.sleep(0.15)
                    else:
                        difficulty = 'medium'
                if (820 <= mouse[0] <= 1070) and (690 <= mouse[1] <= 782):
                    if difficulty == 'hard':
                        dis.blit(checkmark_image, (mouse[0] - 30, mouse[1] - 50))
                        pygame.display.flip(), time.sleep(0.15)
                    else:
                        difficulty = 'hard'
                if (552 <= mouse[0] <= 1058) and (285 <= mouse[1] <= 495):
                    run_start_menu = False
                    run_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_start_menu = False
                    run_game = True

                print(mouse)
        dis.blit(gradient, (0, 0))

        pygame.draw.rect(
            dis, GBRD_COLOUR_BORDER,
            (
                GBRD_START_X - GBRD_BORDER_THICKNESS, GBRD_START_Y - GBRD_BORDER_THICKNESS, PPT * TILES + 2 * GBRD_BORDER_THICKNESS,
                PPT * TILES + 2 * GBRD_BORDER_THICKNESS)
        )
        draw_game_board(PPT, TILES, GBRD_START_X, GBRD_START_Y)

        dis.blit(snake_image, (95, 240))

        rounded_rectangle(dis, (500, 250, 600, 280), DARK_TURQUOISE)
        space_image = pygame.transform.scale(pygame.image.load('resource_press_space.png'), (509, 209))
        img = dis.blit(space_image, (550, 285))

        rounded_rectangle(dis, (90, 20, 1070, 130), DARK_TURQUOISE, 0.2)
        dis.blit(title_font.render("Isaac's Snake Game", 1, WHITE), (235, 53))

        rounded_rectangle(dis, (90, 640, 1070, 200), (23, 110, 104))
        rounded_rectangle(dis, (100, 650, 1050, 180), GBRD_COLOUR_BORDER)

        mouse = pygame.mouse.get_pos()

        difficulty_text_width, difficulty_text_height = scoreboard_font.size(difficulty.capitalize())

        if difficulty == 'easy':
            rounded_rectangle(dis, (160, 680, 270, 112), GREEN_DARK, 0.2)
            PPT, TILES = 16, 40
            difficulty_colour, difficulty_offset = GREEN, ((SBRD_ITEM_WIDTH / 2) - (difficulty_text_width / 2))

            speed = 6
            snake_speed_limit = 15
            snake_speed_increase_interval = 5
            snake_speed_increase_amount = 1
            walls = 40

        elif difficulty == 'medium':
            rounded_rectangle(dis, (490, 680, 270, 112), YELLOW_DARK, 0.2)
            PPT, TILES = 32, 20
            difficulty_colour, difficulty_offset = YELLOW, ((SBRD_ITEM_WIDTH / 2) - (difficulty_text_width / 2))

            speed = 6
            snake_speed_limit = 10
            snake_speed_increase_interval = 10
            snake_speed_increase_amount = 1
            walls = 10

        elif difficulty == 'hard':
            rounded_rectangle(dis, (810, 680, 270, 112), RED_DARK, 0.2)
            PPT, TILES = 64, 10
            difficulty_colour, difficulty_offset = RED, ((SBRD_ITEM_WIDTH / 2) - (difficulty_text_width / 2))

            speed = 5
            snake_speed_limit = 6
            snake_speed_increase_interval = 50
            snake_speed_increase_amount = 1
            walls = 4

        if ((170 <= mouse[0] <= 420) and (690 <= mouse[1] <= 782)) and difficulty != 'easy':
            rounded_rectangle(dis, (170, 690, 250, 92), GREEN_DARK, 0.2)
            dis.blit(button_font.render("Easy", 1, WHITE_DARK), (240, 713))
        else:
            rounded_rectangle(dis, (170, 690, 250, 92), GREEN, 0.2)
            dis.blit(button_font.render("Easy", 1, WHITE), (240, 713))

        if ((500 <= mouse[0] <= 750) and (690 <= mouse[1] <= 782)) and difficulty != 'medium':
            rounded_rectangle(dis, (500, 690, 250, 92), YELLOW_DARK, 0.2)
            dis.blit(button_font.render("Medium", 1, WHITE_DARK), (535, 713))
        else:
            rounded_rectangle(dis, (500, 690, 250, 92), YELLOW, 0.2)
            dis.blit(button_font.render("Medium", 1, WHITE), (535, 713))

        if ((820 <= mouse[0] <= 1070) and (690 <= mouse[1] <= 782)) and difficulty != 'hard':
            rounded_rectangle(dis, (820, 690, 250, 92), RED_DARK, 0.2)
            dis.blit(button_font.render("Hard", 1, WHITE_DARK), (885, 713))
        else:
            rounded_rectangle(dis, (820, 690, 250, 92), RED, 0.2)
            dis.blit(button_font.render("Hard", 1, WHITE), (885, 713))

        pygame.display.flip()

    ###############################################
    #                                             #
    #                  THE MAIN                   #
    #                  GAME LOOP                  #
    #                                             #
    ###############################################

    if run_game:
        food_pos = GBRD_START_X + PPT * (random.randint(1, TILES - 1)), GBRD_START_Y + PPT * (random.randint(0, TILES - 1))

        walls_pos = []
        genned_walls = 0

        while genned_walls < walls:

            gen_wall = [GBRD_START_X + PPT * (random.randint(1, TILES - 1)), GBRD_START_Y + PPT * (random.randint(0, TILES - 1))]
            if gen_wall[0] == food_pos[0] and gen_wall[1] == food_pos[1]:
                pass
            elif gen_wall[0] <= GBRD_START_X + PPT * 3:
                pass
            else:
                walls_pos.append(gen_wall)
                genned_walls += 1

        snake_pos = [GBRD_START_X + PPT, GBRD_START_Y + PPT * (random.randint(1, TILES - 2))]
        food_timer = time_per_food
        snake_body = [[-100, -100], [-100, -100], [-100, -100]]
        direction = '→'
        score = 0  # Setting the initial score to 0
        food = 0  # Setting the initial food to 0
        timer_colour = GREEN  # Setting the initial timer colour
        current_colour = SNAKE_START_RED_VALUE
        game_timer = 0
        time_since_food = 0
        intro = None

    while run_game:


        ###############################################
        #         EVENT RELATED CALCULATIONS          #
        ###############################################

        # For each event triggered

        if intro == "run":
            pygame.mixer.Sound.play(countdown_sound)
            dis.blit(countdown_font.render("3", 1, WHITE), (590, 180))
            pygame.display.flip(), time.sleep(0.6)

            dis.blit(countdown_font.render("2", 1, WHITE), (590, 330))
            pygame.display.flip(), time.sleep(0.6)

            dis.blit(countdown_font.render("1", 1, WHITE), (600, 480))
            pygame.display.flip(), time.sleep(0.6)

            pygame.mixer.music.play(-1)

            dis.blit(countdown_font.render("GO", 1, WHITE), (555, 630))
            pygame.display.flip(), time.sleep(0.6)
            intro = "null"


        for event in pygame.event.get():

            # If they click the quit button
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()

            # If they click a key
            if event.type == pygame.KEYDOWN:
                # Setting the direction, checking if it's equal to their negative direction and not allowing them to change if it is
                direction = '↑' if (event.key == ord('w') or event.key == pygame.K_UP) and direction != '↓' else direction
                direction = '←' if (event.key == ord('a') or event.key == pygame.K_LEFT) and direction != '→' else direction
                direction = '↓' if (event.key == ord('s') or event.key == pygame.K_DOWN) and direction != '↑' else direction
                direction = '→' if (event.key == ord('d') or event.key == pygame.K_RIGHT) and direction != '←' else direction

            # Setting up the timer(s)
            if event.type == pygame.USEREVENT:
                if not food_timer < 0.01: food_timer -= 0.01
                time_since_food += 0.01
                game_timer += 0.01

        # Moving the snake / registering the direction change
        if direction == '↑': snake_pos[1] -= PPT
        if direction == '↓': snake_pos[1] += PPT
        if direction == '←': snake_pos[0] -= PPT
        if direction == '→': snake_pos[0] += PPT

        ###############################################
        #          FOOD RELATED CALCULATIONS          #
        ###############################################

        # If the location of a piece of food matches the location of the Snake
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            pygame.mixer.Sound.play(apple_eat_sound)
            if time_since_food < 2:
                time_per_food += 1
                pygame.mixer.Sound.play(power_up_sound)
                time_since_food = 0
            else:
                time_since_food = 0

            # Adding to score, food, and resetting the food timer
            score, food, food_timer = (score_increase_amount + score), (food + 1), time_per_food
            timer_colour = GREEN
            print(f"Score: {score}")

            # Overwriting the display if the score, food exceeds 5 digits long
            if len(str(score)) > 5: score = 99999
            if len(str(food)) > 5: food = 99999

            # Spawning new food, verifying that the spawn isn't inside the snake

            while True:
                found, food_pos = False, (GBRD_START_X + PPT * (random.randint(1, TILES - 1)), GBRD_START_Y + PPT * (random.randint(1, TILES - 1)))  # Randomizing Spawn
                for pos in snake_body:  # Checking if the new spawn is inside the snake's body
                    if (pos[0], pos[1]) == food_pos: found = True
                for w in walls_pos:
                    if food_pos[0] == w[0] and food_pos[1] == w[1]:
                        found = True

                if not found:  # Breaking if it isn't in the snake's body
                    break

            # Increasing the speed every X items eaten
            if speed <= snake_speed_limit and food % snake_speed_increase_interval == 0:
                speed += snake_speed_increase_amount
                pygame.mixer.Sound.play(speed_up_sound)

        # If the snake did NOT eat a piece of food, pop the snake body (THIS IS VERY IMPORTANT, IT'S WHAT CAUSES THE END OF THE SNAKE SEGMENTS TO DISAPPEAR)
        else:
            snake_body.pop()

        # If the snake runs into a wall (lol)
        found_snake_in_wall = False
        for w in walls_pos:
            if snake_pos[0] == w[0] and snake_pos[1] == w[1]: found_snake_in_wall = True

        # If the snake goes out of bounds (lol)
        snake_out_of_bounds = False
        if snake_pos[0] < GBRD_START_X or snake_pos[0] > GBRD_START_X + (PPT * TILES) - 1:  snake_out_of_bounds = True  # X Boundary
        if snake_pos[1] < GBRD_START_Y or snake_pos[1] > GBRD_START_Y + (PPT * TILES) - 1:  snake_out_of_bounds = True  # Y Boundary

        if found_snake_in_wall or snake_out_of_bounds:
            pygame.image.save(dis, "resource_end_game_screen.png")

        ###############################################
        #         DRAWING GRAPHICS TO DISPLAY         #
        ###############################################

        if not found_snake_in_wall and not snake_out_of_bounds:
            # Display, Game Board
            dis.blit(gradient, (0, 0))

            pygame.draw.rect(
                dis, GBRD_COLOUR_BORDER,
                (
                    GBRD_START_X - GBRD_BORDER_THICKNESS, GBRD_START_Y - GBRD_BORDER_THICKNESS, PPT * TILES + 2 * GBRD_BORDER_THICKNESS,
                    PPT * TILES + 2 * GBRD_BORDER_THICKNESS)
            )

            draw_game_board(PPT, TILES, GBRD_START_X, GBRD_START_Y)

            # Drawing the Food
            pygame.draw.rect(dis, WHITE, pygame.Rect(food_pos[0], food_pos[1], PPT, PPT))

            # Scoreboard Rectangles
            rounded_rectangle(dis, (sbrd_item_1_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), timer_colour)
            rounded_rectangle(dis, (sbrd_item_2_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), difficulty_colour)
            rounded_rectangle(dis, (sbrd_item_3_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), GBRD_COLOUR_DARK)
            rounded_rectangle(dis, (sbrd_item_4_pos_x, sbrd_coord_y, SBRD_ITEM_WIDTH, SBRD_ITEM_HEIGHT), GBRD_COLOUR_DARK)

            # Timer Scoreboard
            if food_timer < (5 / 10) * time_per_food:  # 10
                timer_colour = YELLOW
                if food_timer < (1 / 3) * time_per_food:  # 7
                    timer_colour = ORANGE
                    if food_timer < (1 / 6) * time_per_food:  # 3
                        timer_colour = RED

            if food_timer >= 1000:
                timer_offset = -24
            elif food_timer >= 100:
                timer_offset = -12
            elif food_timer <= 10:
                timer_offset = 10
            else:
                timer_offset = 0

            dis.blit(timer_image, (sbrd_item_1_pos_x + 40 + timer_offset, sbrd_text_y - 7))
            dis.blit(scoreboard_font.render(f"{round(food_timer, 1)}s", 1, WHITE), (sbrd_coord_x + 95 + timer_offset, sbrd_text_y))

            # Difficulty Scoreboard
            dis.blit(scoreboard_font.render(difficulty.capitalize(), 1, WHITE), (sbrd_item_2_pos_x + difficulty_offset, sbrd_text_y))

            # Score Scoreboard
            score_text = f"Score: {score}"
            score_text_width, score_text_height = scoreboard_font.size(score_text)
            score_text_offset = (SBRD_ITEM_WIDTH - score_text_width) / 2
            dis.blit(scoreboard_font.render(score_text, 1, WHITE), (sbrd_item_3_pos_x + score_text_offset, sbrd_text_y))

            # Food Scoreboard
            food_text = f"x {food}"
            food_text_width, food_text_height = scoreboard_font.size(food_text)
            food_text_offset = (SBRD_ITEM_WIDTH - food_text_width - SBRD_ITEM_4_FOOD_SIZE) / 2

            pygame.draw.rect(dis, WHITE, pygame.Rect(sbrd_item_4_pos_x + food_text_offset, sbrd_text_y, SBRD_ITEM_4_FOOD_SIZE, SBRD_ITEM_4_FOOD_SIZE))  # Drawing the Symbol
            dis.blit(scoreboard_font.render(food_text, 1, WHITE), (sbrd_item_4_pos_x + 40 + food_text_offset, sbrd_text_y))

            snake_body.insert(0, list(snake_pos))  # Snake Values Constructor

            # Generating Snake Colour & Drawing Snake
            flip = False  # Setting the flip-flop

            for pos in snake_body:  # Iterating through the snake
                if flip:  # Subtracting red value if "Flip = True"
                    current_colour, flip = (current_colour + snake_colour_interval, flip) if current_colour + snake_colour_interval < 225 else (
                        current_colour - snake_colour_interval, False)
                else:  # Adding red value if "Flip = False"
                    current_colour, flip = (current_colour - snake_colour_interval, flip) if current_colour - snake_colour_interval > 81 else (
                        current_colour + snake_colour_interval, True)

                pygame.draw.rect(dis, (current_colour, 45, 180), pygame.Rect(pos[0], pos[1], PPT, PPT))  # Drawing the Segment
            pygame.draw.rect(dis, SNAKE_COLOUR_HEAD, pygame.Rect(snake_pos[0], snake_pos[1], PPT, PPT))  # Overwriting the Head

            # Drawing the Walls
            for w in walls_pos:
                pygame.draw.rect(dis, DARK_TURQUOISE, pygame.Rect(w[0], w[1], PPT, PPT))

        ###############################################
        #    CHECKING BOUNDS - END GAME CONDITIONS    #
        ###############################################

        # If the snake exits the map
        if snake_out_of_bounds:
            run_game = False
            pygame.mixer.Sound.play(wall_crash_sound)

        # If the snake cuts into itself
        for segment in snake_body[1:]:  # For each segment
            if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:  run_game = False  # If the segment overlaps with another

        # If the score, food are >= 99,999
        if score >= 99999 or food >= 99999:
            if score >= 99999: score = 99999
            if food >= 99999: food = 99999
            run_game = False

        # If the food timer hits 0.0 seconds
        if food_timer < 0.01: run_game = False

        # If the snake runs into a wall
        if found_snake_in_wall:
            pygame.mixer.Sound.play(wall_crash_sound)
            run_game = False

        if intro is None:
            intro = "run"

        ###############################################
        #             GAME/DISPLAY UPDATES            #
        ###############################################

        pygame.display.flip()  # Update Text
        pygame.display.update()  # Update Display
        fps_controller.tick(speed)

        if not run_game:
            if not found_snake_in_wall and not snake_out_of_bounds:
                pygame.image.save(dis, "resource_end_game_screen.png")
            run_end_menu = True

    if run_end_menu:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(game_over_sound)

        # High Scores
        file = open("./resource_highscore.txt", "r")

        raw_high_scores = file.read()
        file.close()

        high_score_constructor = ""
        high_scores = []

        print(raw_high_scores)
        for char in raw_high_scores:
            if not char == ":":
                high_score_constructor += char
            else:
                high_scores.append(high_score_constructor)
                high_score_constructor = ""

        hs_range = None

        if difficulty == 'easy':
            hs_range = 0
            high_score = high_scores[hs_range]
        elif difficulty == 'medium':
            hs_range = 1
            high_score = high_scores[hs_range]
        elif difficulty == 'hard':
            hs_range = 2
            high_score = high_scores[hs_range]

        if int(high_score) < score:
            high_scores[hs_range] = score
            print(high_scores)
            for idx, i in enumerate(high_scores):
                high_scores[idx] = str(i)

            file = open("./resource_highscore.txt", "w")
            file.write(":".join(high_scores) + ":")
            file.close()
            new_or_not = "NEW!"
        else:
            new_or_not = ""

    while run_end_menu:

        for event in pygame.event.get():

            # If they click the quit button
            if event.type == pygame.QUIT:
                os.remove("resource_end_game_screen.png")
                pygame.quit(), sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()

                if (40 <= mouse[0] <= 260) and (684 <= mouse[1] <= 774):
                    run_end_menu = False
                    run_start_menu = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_end_menu = False
                    run_start_menu = True

        # End Graphics

        dis.blit(pygame.image.load('resource_end_game_screen.png'), (0, 0))

        rounded_rectangle(dis, (20, 20, 1220, 130), DARK_TURQUOISE, 0.2)
        dis.blit(title_font.render("Game Over", 1, WHITE), (415, 50))

        rounded_rectangle(dis, (20, 200, 260, 600), TURQUOISE, 0.2)

        # High Score
        dis.blit(end_screen_font.render("HIGH SCORE", 1, WHITE), (55, 230))
        dis.blit(scoreboard_font.render(f"{high_scores[hs_range]} {new_or_not}", 1, WHITE_DARK), (55, 280))

        # High Score
        dis.blit(end_screen_font.render("YOUR SCORE", 1, WHITE), (55, 350))
        dis.blit(scoreboard_font.render(f"{score}", 1, WHITE_DARK), (55, 400))

        # Food Eaten
        dis.blit(end_screen_font.render("FOOD EATEN", 1, WHITE), (55, 460))
        pygame.draw.rect(dis, WHITE_DARK, pygame.Rect(55, 510, SBRD_ITEM_4_FOOD_SIZE, SBRD_ITEM_4_FOOD_SIZE))  # Drawing the Symbol
        dis.blit(scoreboard_font.render(f"x {food}", 1, WHITE_DARK), (95, 510))

        # High Score
        dis.blit(end_screen_font.render("GAME TIME", 1, WHITE), (55, 580))
        dis.blit(scoreboard_font.render(f"{parse_time(game_timer)}", 1, WHITE_DARK), (55, 630))

        # Replay Button
        dis.blit(replay_image, (39, 685))
        dis.blit(snake_image, (800, 310))
        pygame.display.flip()
