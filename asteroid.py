import circleshape
from constants import LINE_WIDTH
from pygame.draw import circle

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface, color="white", width=LINE_WIDTH):
        circle(surface, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)