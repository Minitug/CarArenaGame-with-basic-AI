from core.car_env import CarEnv
# from core.physics import update_car
from rendering.renderer import draw
import pygame

def get_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "QUIT"

    keys = pygame.key.get_pressed()
    throttle = 0
    steering = 0

    if keys[pygame.K_w]:
        throttle += 1
    if keys[pygame.K_s]:
        throttle -= 1
    if keys[pygame.K_a]:
        steering -= 1
    if keys[pygame.K_d]:
        steering += 1
    if keys[pygame.K_BACKSPACE]:
        return "RESET"
    if keys[pygame.K_ESCAPE]:
        return "QUIT"

    return throttle, steering

MAX_SCREEN_WIDTH = 1920
MAX_SCREEN_HEIGHT = 1080

new_env_width = 3000
new_env_height = 2500
new_env_verbose = True
new_env_players = 1
new_env_max_cars = 1
if new_env_width > MAX_SCREEN_WIDTH:
    new_env_width = MAX_SCREEN_WIDTH
if new_env_height > MAX_SCREEN_HEIGHT:
    new_env_height = MAX_SCREEN_HEIGHT
new_env_spawn = (new_env_width // 2, new_env_height // 2)

# create window
pygame.init()
screen = pygame.display.set_mode((new_env_width, new_env_height))
pygame.display.set_caption("Car Arena")

clock = pygame.time.Clock()
running = True

# create env
env = CarEnv(width = new_env_width, height = new_env_height, spawn = new_env_spawn, players = new_env_players, max_cars = new_env_max_cars, verbose = new_env_verbose)



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

pygame.quit()