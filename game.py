# import pygame module in this program
import pygame
from keyboard import Keyboard
from player import Player
from phase import Phase
from files import Files
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()


# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((500, 500))

# set the pygame window name
pygame.display.set_caption("Moving rectangle")
# imp = pygame.image.load("images\phase_0.png").convert()

# paint screen one time
pygame.display.flip()
f = Files()
phases = f.load_from_file("./phases.csv")

# define a variable to control the score text
font = pygame.font.Font(None, 36)

# define a variable to control the instruction text
font_instruction = pygame.font.Font(None, 32)

# Set the starting score
score = 0

instructions = ['Welcome to the moving rectangle game!',
                'Use the arrow keys to move your character.',
                'Complete the shape in the background to win!',
                'Avoid the enemies or you will lose.',
                'Press SPACE to continue.']

# Render the instructions text as a list of surfaces
instruction_surfaces = []

for text in instructions:
    instruction_surfaces.append(font_instruction.render(
        text, True, (136, 206, 250)))

# define the RGB value
# for white, green,
# blue, black, red
# colour respectively.
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)

# Using blit to copy content from one surface to other
win.blit(phases[0].background, phases[0].pos)

# Indicates pygame is running
run = True
started = False

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
    run, started = Keyboard.keyboard_callback(
        keys, run, started, phase)

    # completely fill the surface object
    # with black colour
    win.fill(black)
    win.blit(phase.background, phase.pos)

    # paint screen one time
    # pygame.display.flip()

    # drawing object on screen which is rectangle here
    pygame.draw.rect(win, phase.player.color, phase.player.rect)

    for enemy in phase.enemies:
        pygame.draw.rect(win, enemy.color, enemy.rect)

    if not started:
        # Fill the screen with black
        win.fill(black)
        
        # Set the y-coordinate for the top of the first instruction
        instruction_y = 150

        # Draw the instructions text on the screen
        for surface in instruction_surfaces:
            win.blit(surface, (10, instruction_y))
            instruction_y += 24 + 15

    # add the score to the screen
    score_text = font.render('Score: {}'.format(score), True, (255, 255, 255))
    win.blit(score_text, (10, 10))

    # it refreshes the window
    pygame.display.update()

    if phase.detect_collision():
        score = 0

    if phase.tolerance_ok():
        score += 100
        actual_phase += 1
        if actual_phase >= len(phases):
            run = False

# closes the pygame window
pygame.quit()
