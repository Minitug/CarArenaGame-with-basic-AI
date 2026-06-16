import pygame
from core.car_env import CarEnv


def draw(screen, env: CarEnv):
    screen.fill((0, 0, 0))
    for car in env.cars:
        pygame.draw.rect(screen, (255, 0, 0), (car.position.x, car.position.y, car.LENGTH, car.WIDTH))
    pygame.display.flip()