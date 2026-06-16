import pygame
from core.car_env import CarEnv

def draw(screen, env: CarEnv, font):
    screen.fill((0, 0, 0))
    for car in env.cars:
        text = font.render(f"Speed: {car.speed:.2f}", True, (255, 255, 255))
        screen.blit(text, (car.position.x, car.position.y - 30))
        pygame.draw.rect(screen, (255, 0, 0), (car.position.x, car.position.y, car.LENGTH, car.WIDTH))
    pygame.display.flip()
