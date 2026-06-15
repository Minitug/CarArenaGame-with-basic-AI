from pygame.math import Vector2

class Car:

    MAX_SPEED = 400
    MAX_ACCELERATION = 240
    WIDTH = 190
    LENGTH = 340
    MAX_STEERING_ANGLE = 1
    STEERING_SPEED = 120
    STEERING_RETURN_SPEED = 180


    def __init__(self, x, y):
        # self.x = x
        # self.y = y
        self.position = Vector2(x, y)
        self.speed = 0
        self.heading = 0
        self.throttle = 0
        self.steering = 0

    def set_controls(self, throttle, steering):
        self.throttle = max(-1, min(1, throttle))
        self.steering = max(-1, min(1, steering))

    def reset(self, x, y):
        self.position = Vector2(x, y)
        self.speed = 0
        self.heading = 0
        self.throttle = 0
        self.steering = 0