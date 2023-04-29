import pygame


def keyboard_callback(keys, x, y, run, vel=10, height=20, width=20):
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:

        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500-width:

        # increment in x co-ordinate
        x += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:

        # decrement in y co-ordinate
        y -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500-height:
        # increment in y co-ordinate
        y += vel

    if keys[pygame.K_ESCAPE]:
        run = False
    return x, y, run
