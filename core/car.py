from pygame.math import Vector2

class Car:

    MAX_SPEED = 400
    MAX_REVERSE_SPEED = -80
    MAX_ACCELERATION = 240
    MAX_REVERSE_ACCELERATION = MAX_ACCELERATION / 3
    BRAKE_FORCE = MAX_ACCELERATION / 2
    WIDTH = 19
    LENGTH = 34
    MAX_STEERING_ANGLE = 35
    STEERING_SPEED = 120
    STEERING_RETURN_SPEED = STEERING_SPEED * 1.5
    TURN_RATE = 110 
    FRICTION = 80
    TURNING_DRAG = 0.5



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