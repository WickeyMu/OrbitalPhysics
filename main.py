import pygame
import math

pygame.init()

GRAVITATIONAL_CONSTANT = 6.673

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Circle:
    def __init__(self, x, y, r, m, res, x_vel, y_vel):
        self.x = x
        self.y = y
        self.radius = r
        self.mass = m
        self.restitution = res
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y,), self.radius, 1)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


def draw():
    screen.fill((0, 0, 0))
    circle.draw(screen)
    planet.draw(screen)


def calculate_gravity_acceleration(object_one, object_two):
    x_dist = object_one.x - object_two.x
    y_dist = object_one.y - object_two.y

    distance = math.sqrt((x_dist ** 2) + (y_dist ** 2))
    if distance == 0:
        return 0
    gravity_accel = (object_one.mass * GRAVITATIONAL_CONSTANT) / (distance ** 2)

    return gravity_accel


def calculate_gravity(object_one, object_two, accel):
    x_dist = object_one.x - object_two.x
    y_dist = object_one.y - object_two.y

    angle = math.atan2(y_dist, x_dist)

    x_change = math.cos(angle) * accel
    y_change = math.sin(angle) * accel

    return x_change, y_change


def enact_gravity(object_one, object_two):
    accel = calculate_gravity_acceleration(object_one, object_two)
    vector_change = calculate_gravity(object_one, object_two, accel)

    object_two.x_vel += vector_change[0]
    object_two.y_vel += vector_change[1]


def collision(object_one, object_two):
    x_dist = object_one.x - object_two.x
    y_dist = object_one.y - object_two.y

    distance = math.sqrt((x_dist ** 2) + (y_dist ** 2))

    if distance <= (object_one.radius + object_two.radius):
        return True


def bounce(obj_one, obj_two):
    delta_pos = (obj_one.x - obj_two.x, obj_one.y - obj_two.y)
    dist = math.sqrt(delta_pos[0] ** 2 + delta_pos[1] ** 2)

    if dist == 0:
        return

    normal = [delta_pos[0] / dist, delta_pos[1] / dist]

    delta_vel = (obj_one.x_vel - obj_two.x_vel, obj_one.y_vel - obj_two.y_vel)

    vel_normal = delta_vel[0] * normal[0] + delta_vel[1] * normal[1]

    if vel_normal > 0:
        return

    combined_restitution = (obj_one.restitution + obj_two.restitution) / 2

    impulse_mag = -(1 + combined_restitution) * vel_normal
    impulse_mag /= (1 / obj_one.mass + 1 / obj_two.mass)

    impulse = (impulse_mag * normal[0], impulse_mag * normal[1])

    obj_one.x_vel += impulse[0] / obj_one.mass
    obj_one.y_vel += impulse[1] / obj_one.mass

    obj_two.x_vel -= impulse[0] / obj_two.mass
    obj_two.y_vel -= impulse[1] / obj_two.mass


circle = Circle(400, 400, 50, 50, 1, 0, 0)
planet = Circle(400, 200, 20, 20, 1, 0, 0)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()

    enact_gravity(circle, planet)
    enact_gravity(planet, circle)

    if collision(circle, planet):
        bounce(circle, planet)

    circle.move()
    planet.move()

    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()