from pygame.math import Vector2

class Car:

    MAX_SPEED = 400
    MAX_ACCELERATION = 240
    WIDTH = 190
    LENGTH = 340
    MAX_STEERING_ANGLE = 35
    STEERING_SPEED = 120
    STEERING_RETURN_SPEED = 180
    TURN_RATE = 180


    def __init__(self, position):
        self.position = Vector2(position)
        self.speed = 0
        self.heading = 0
        self.throttle = 0
        self.steering = 0
        self.steering_angle = 0

    def set_controls(self, throttle, steering):
        self.throttle = max(-1, min(1, throttle))
        self.steering = max(-1, min(1, steering))

    def reset(self, position):
        self.position = Vector2(position)
        self.speed = 0
        self.heading = 0
        self.throttle = 0
        self.steering = 0
        self.steering_angle = 0