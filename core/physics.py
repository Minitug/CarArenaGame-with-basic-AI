# physics.py

def update_car(car, dt):
    apply_acceleration(car, dt)
    apply_steering(car, dt)
    move_car(car, dt)


def apply_acceleration(car, dt):
    acceleration_factor = 1 - (car.speed / car.MAX_SPEED)
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

def rotate_car(car, dt):
    turn_strength = car.steering_angle / car.MAX_STEERING_ANGLE
    car.heading += turn_strength * car.TURN_RATE

def move_car(car, dt):
    if abs(car.speed) <0.01:
        car.speed = 0
    direction = Vector2(1, 0)
    direction.rotate_ip(car.heading)
    car.position += direction * car.speed * dt
    car.heading += (car.steering_angle * car.TURN_RATE * dt)