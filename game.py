# import pygame module in this program
import pygame
from keyboard import Keyboard
from player import Player
from phase import Phase
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))


# set the pygame window name
pygame.display.set_caption("Moving rectangle")
#imp = pygame.image.load("images\phase_0.png").convert()

# paint screen one time
pygame.display.flip()

# define the RGB value
# for white, green,
# blue, black, red
# colour respectively.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

player = Player(200, 200, red, 20, 20, 0.5)
phase0 = Phase(player, "images\phase_0.png", (0, 0), (389.0, 89.5))
phase1 = Phase(player, "images\phase_1.png", (0, 0), (190.0, 322.0))
phases = [phase0, phase1]
# Using blit to copy content from one surface to other
win.blit(phases[0].background, phases[0].pos)
# object current co-ordinates
x = 200
y = 200

# dimensions of the object
width = 20
height = 20

# velocity / speed of movement
vel = 0.5

# Indicates pygame is running
run = True
actual_phase = 0
# infinite loop
while run:
    phase = phases[actual_phase]
    # creates time delay of 10ms
    pygame.time.delay(10)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()
    run = Keyboard.keyboard_callback(
        keys, run, phase)

    # completely fill the surface object
    # with black colour
    win.fill(black)
    win.blit(phase.background, phase.pos)

    # paint screen one time
    # pygame.display.flip()

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, phase.player.color, (phase.player.x,
                     phase.player.y, phase.player.width, phase.player.height))

    # it refreshes the window
    pygame.display.update()
    print(phase.player.x)
    print(phase.player.y)
    if (phase.player.x, phase.player.y) == phase.end_pos:
        actual_phase += 1
        if actual_phase >= len(phases):
            run = False

# closes the pygame window
pygame.quit()
