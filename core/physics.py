from pygame.math import Vector2

def update_car(car, dt):
    apply_acceleration(car, dt)
    apply_friction(car, dt)
    apply_steering(car, dt)
    rotate_car(car, dt)
    move_car(car, dt)


def apply_acceleration(car, dt):
    if car.throttle > 0:
        acceleration_factor = 1 - (car.speed / car.MAX_SPEED)
    else:
        acceleration_factor = 1 - (car.speed / car.MAX_REVERSE_SPEED)
    car.speed += car.throttle * car.MAX_ACCELERATION * acceleration_factor * dt


def apply_steering(car, dt):
    target_angle = car.steering * car.MAX_STEERING_ANGLE

    if car.steering != 0:
        rate = car.STEERING_SPEED
    else:
        rate = car.STEERING_RETURN_SPEED
    
    if car.steering_angle < target_angle:
        car.steering_angle = min(car.steering_angle + rate * dt, target_angle)
    elif car.steering_angle > target_angle:
        car.steering_angle = max(car.steering_angle - rate * dt, target_angle)

    current_turning_drag = car.TURNING_DRAG * abs(car.steering_angle / car.MAX_STEERING_ANGLE)
    car.speed *= (1 - current_turning_drag * dt)

def rotate_car(car, dt):
    if car.speed == 0:
        return
    speed_ratio = (car.speed) / car.MAX_SPEED

    turn_strength = car.steering_angle / car.MAX_STEERING_ANGLE * (1 - speed_ratio)
    car.heading += turn_strength * car.TURN_RATE * dt

def move_car(car, dt):
    if abs(car.speed) <0.01:
        car.speed = 0

    direction = Vector2(1, 0)
    direction.rotate_ip(car.heading)
    car.position += direction * car.speed * dt

def apply_friction(car, dt):
    this_friction = car.FRICTION
    if car.throttle != 0:
        this_friction = car.FRICTION * 0.05
    if car.speed > 0:
        car.speed = max(car.speed - this_friction * dt, 0)
    elif car.speed < 0:
        car.speed = min(car.speed + this_friction * dt, 0)