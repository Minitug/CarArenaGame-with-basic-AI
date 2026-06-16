from pygame.math import Vector2
from core.car import Car
from core.physics import update_car

class CarEnv:
    def __init__(self, width, height, spawn, verbose=True, players = 1, max_cars = 4):
        self.width = width
        self.height = height
        self.spawn = Vector2(spawn)
        self.verbose = verbose
        self.players = players
        self.max_cars = max_cars
        self.cars = self.create_cars()


    def create_cars(self):
        cars = []
        for i in range(self.max_cars):
            cars.append(Car(position=self.spawn))
        return cars

    def reset(self):
        for car in self.cars:
            car.reset(position=self.spawn)

    def step(self, action, dt):
        for car in self.cars:
            car.set_controls(*action)
            update_car(car, dt)