import pygame
from phase import Phase


class Keyboard:
    def keyboard_callback(keys, run, phase):
        # if left arrow key is pressed
        if keys[pygame.K_LEFT] and phase.player.x > 0:

            # decrement in x co-ordinate
            phase.player.update_pos(-phase.d_x, 0)

        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and phase.player.x < 500-phase.player.width:

            # increment in x co-ordinate
            phase.player.update_pos(phase.d_x, 0)

        # if left arrow key is pressed
        if keys[pygame.K_UP] and phase.player.y > 0:

            # decrement in y co-ordinate
            phase.player.update_pos(0, -phase.d_y)

        # if left arrow key is pressed
        if keys[pygame.K_DOWN] and phase.player.y < 500-phase.player.height:
            # increment in y co-ordinate
            phase.player.update_pos(0, phase.d_y)

        if keys[pygame.K_ESCAPE]:
            run = False
        return run
