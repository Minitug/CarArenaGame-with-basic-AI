import pygame
from core.car_env import CarEnv

def draw(screen, env: CarEnv, font):
    screen.fill((0, 0, 0))

    for car in env.cars:
        
        car_surface = pygame.Surface((car.LENGTH, car.WIDTH), pygame.SRCALPHA)

        pygame.draw.rect(
            car_surface,
            (255, 0, 0),
            (0, 0, car.LENGTH, car.WIDTH)
        )

        rotated_surface = pygame.transform.rotate(car_surface, -car.heading)

        rotated_rect = rotated_surface.get_rect(
            center=(car.position.x, car.position.y)
        )

        screen.blit(rotated_surface, rotated_rect.topleft)
        
        text = font.render(f"Speed: {car.speed:.2f} km/h", True, (255, 255, 255))
        screen.blit(text, (screen.get_width() - text.get_width() - 20, screen.get_height() - text.get_height() - 20))
    pygame.display.flip()
