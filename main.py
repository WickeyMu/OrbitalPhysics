import pygame

pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Circle:
    def __init__(self, x, y, r, x_vel, y_vel):
        self.x = x
        self.y = y
        self.radius = r
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


circle = Circle(400, 400, 50, 0, 0)
planet = Circle(200, 200, 20, 0, 0)

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
