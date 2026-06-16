from core.car_env import CarEnv
from core.physics import update_car
from rendering.renderer import draw
import pygame

# create window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car Arena")

clock = pygame.time.Clock()
running = True

# create env
env = CarEnv()



# loop:
#     get dt
#     read keyboard
#     env.step(...)
#     draw(...)

while running:
    dt = clock.tick(60) / 1000  

    action = get_input()
    if action == "QUIT":
        running = False
    elif action == "RESET":
        env.reset()
    else:
        env.step(action, dt)

    draw(screen, env)
