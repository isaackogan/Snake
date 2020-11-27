from pygame import *


def rounded_rectangle(r_surface, r_rect, r_colour, r_radius=0.6):  # A simple function to create a rounded rectangle
    """Creates a rounded rectangle on a given surface.

    :param r_surface: The surface in which the rounded rectangle will be drawing on
    :param r_rect: The rectangle's information such as x-coordinate, y-coordinate width, height in a tuple
    :param r_colour: The RGB (or RGBA) colour
    :param r_radius: The curve of the rectangle
    :return: Returns the blitted object
    """

    # Declarations/ Definitions
    r_rect = Rect(r_rect)           # Defining it as a Rect object
    r_colour = Color(*r_colour)     # Defining its a color object
    alpha = r_colour.a              # Also accepting alpha (RGBA)
    r_colour.a = 0                  # Setting def. value
    pos = r_rect.topleft            # Setting position to top left
    r_rect.topleft = 0, 0           # 0, 0
    rectangle = Surface(r_rect.size, SRCALPHA)  # Working with the provided "Surface" to create rectangle information

    # Calculations
    circle = Surface([min(r_rect.size) * 3] * 2, SRCALPHA)  # Calculating circle
    draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)   # Calculating ellipse
    circle = transform.smoothscale(circle, [int(min(r_rect.size) * r_radius)] * 2)  # Calculating transformations w/ the circle to create rounded edges

    # Blitting
    r_radius = rectangle.blit(circle, (0, 0))   # Blitting based on radius in initial value (top left)

    r_radius.bottomright = r_rect.bottomright   # Going to bottom right
    rectangle.blit(circle, r_radius)            # Blitting based on radius

    r_radius.topright = r_rect.topright         # Going to top right
    rectangle.blit(circle, r_radius)            # Blitting based on radius

    r_radius.bottomleft = r_rect.bottomleft     # Going to bottom left
    rectangle.blit(circle, r_radius)            # Blitting based on radius

    # Filling
    rectangle.fill((0, 0, 0), r_rect.inflate(-r_radius.w, 0))   # Filling area via radius
    rectangle.fill((0, 0, 0), r_rect.inflate(0, -r_radius.h))   # Filling more area via radius
    rectangle.fill(r_colour, special_flags=BLEND_RGBA_MAX)      # More filling
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)   # Final Filling

    # Blitting, returning the resulting surface
    return r_surface.blit(rectangle, pos)
