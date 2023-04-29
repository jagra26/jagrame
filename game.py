# import pygame module in this program
import pygame
import keyboard

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")
imp = pygame.image.load("images\phase_0.png").convert()
# Using blit to copy content from one surface to other
win.blit(imp, (0, 0))

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

# infinite loop
while run:
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
    x, y, run = keyboard.keyboard_callback(
        keys, x, y, run, vel=vel, height=height, width=width)

    # completely fill the surface object
    # with black colour
    win.fill((0, 0, 0))
    win.blit(imp, (0, 0))

    # paint screen one time
    # pygame.display.flip()

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))

    # it refreshes the window
    pygame.display.update()
    # print(x)
    # print(y)
    if x == 389.0 and y == 89.5:
        run = False

# closes the pygame window
pygame.quit()
