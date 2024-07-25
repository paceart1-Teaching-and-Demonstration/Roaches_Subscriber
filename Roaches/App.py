import pygame as py
import Light
import Roach
import random

# Constants
SCREENWIDTH = 480
SCREENHEIGHT = 600
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
FRAMERATE = 30
SCREENCOLOR = (0, 0, 0)

# Set up game

# Initialize game variables
clock = py.time.Clock()
screen = py.display.set_mode(SCREENSIZE)

# Set up game
roach_count = 20
GameLight = Light.Light()
roaches = []

for ii in range(roach_count):
    rand_x = random.randint(0, SCREENWIDTH)
    rand_y = random.randint(0, SCREENHEIGHT)
    r = Roach.Roach(screen, rand_x, rand_y)
    roaches.append(r)
    GameLight.subscribe(r)


# Event Functions
def on_space_key_pressed():
    GameLight.flip_switch()


py.init()

# Main Game Loop
app_running = True
while app_running:
    # Handle Events
    for event in py.event.get():
        if event.type == py.QUIT:
            app_running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                on_space_key_pressed()

    # Draw
    screen.fill(GameLight.get_light_color())
    for r in roaches:
        r.draw()
        r.run_current_behavior()

    py.display.flip()
    # Update
   
    clock.tick(FRAMERATE)
