from modules.settings import *


def draw_game_board(d_PPT, d_TILES, GRID_START_X, GRID_START_Y):  # Draws the game board in a checker pattern (NOT including the border)
    """Draw a checkered game board

    :param d_PPT: The amount of pixels per tile
    :param d_TILES: The amount of d_TILES on the board
    :param GRID_START_X: The start X-position of the grid
    :param GRID_START_Y: The start Y-position of the grid
    """

    pygame.draw.rect(dis, WHITE, (GRID_START_X, GRID_START_Y, d_PPT, d_PPT))  # Drawing the initial rectangle
    current_x, current_y, counter = GRID_START_X, GRID_START_Y, 0  # Setting the initial counter values

    while current_y < ((d_PPT * d_TILES) + GRID_START_Y):  # How far down the rows go/how many they are

        if current_x < ((d_PPT * d_TILES) + GRID_START_X):  # The checker pattern for each individual row
            if (counter % 2) == 0:  # Flip
                pygame.draw.rect(dis, GBRD_COLOUR_LIGHT, (current_x, current_y, d_PPT, d_PPT))  # Light checker colour
            if (counter % 2) != 0:  # Flop
                pygame.draw.rect(dis, GBRD_COLOUR_DARK, (current_x, current_y, d_PPT, d_PPT))  # Dark checker colour
            counter += 1  # Adding to the counter
            current_x += d_PPT  # Adding to the current X based on d_PPT
        else:
            current_x = GRID_START_X  # Resetting the current X at the end of the row
            current_y += d_PPT  # Adding to the current Y at the end of the row (to start a new row)
            counter += 1  # Adding to the counter so that the next row starts w/ a different colour (to keep the checker pattern going)
