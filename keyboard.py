import pygame
from phase import Phase


class Keyboard:
    def keyboard_callback(keys, run, started, phase):
        # if left arrow key is pressed
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and phase.player.rect.x > 0:
            started = True
            # decrement in x co-ordinate
            phase.player.update_pos(-phase.d_x, 0)

        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and phase.player.rect.x < 500-phase.player.width:
            started = True
            # increment in x co-ordinate
            phase.player.update_pos(phase.d_x, 0)

        # if left arrow key is pressed
        if keys[pygame.K_UP] or keys[pygame.K_w] and phase.player.rect.y > 0:
            started = True
            # decrement in y co-ordinate
            phase.player.update_pos(0, -phase.d_y)

        # if left arrow key is pressed
        if keys[pygame.K_DOWN] or keys[pygame.K_s] and phase.player.rect.y < 500-phase.player.height:
            started = True
            # increment in y co-ordinate
            phase.player.update_pos(0, phase.d_y)

        if keys[pygame.K_ESCAPE]:
            run = False

        if keys[pygame.K_SPACE]:
            started = True

        return run, started
