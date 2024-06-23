import pygame
import math

pygame.init()

GRAVITATIONAL_CONSTANT = 6673

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Circle:
    def __init__(self, x, y, r, m, x_vel, y_vel):
        self.x = x
        self.y = y
        self.radius = r
        self.mass = m
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

    gravity_accel = (object_one.mass * GRAVITATIONAL_CONSTANT) / (distance ** 2)

    return gravity_accel


def calculate_gravity_direction(object_one, object_two, accel):
    x_dist = object_one.x - object_two.x
    y_dist = object_one.y - object_two.y

    try:
        ang = math.degrees(math.atan(x_dist / y_dist))
    except ZeroDivisionError:
        if x_dist < 0:
            ang = -90
        else:
            ang = 90

    x_change = math.sin(math.radians(ang)) * accel
    y_change = math.cos(math.radians(ang)) * accel

    if y_dist < 0:
        x_change = x_change * -1
        y_change = y_change * -1

    return x_change, y_change


def enact_gravity(object_one, object_two):
    accel = calculate_gravity_acceleration(object_one, object_two)
    vector_change = calculate_gravity_direction(object_one, object_two, accel)

    object_two.x_vel += vector_change[0]
    object_two.y_vel += vector_change[1]


circle = Circle(400, 400, 50, 50, 0, 0)
planet = Circle(200, 200, 20, 20, 0, 0)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()

    circle.move()
    planet.move()

    pygame.time.delay(10)
    pygame.display.update()
