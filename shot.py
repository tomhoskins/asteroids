from circleshape import CircleShape
from pygame.draw import circle
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface, color="white", width=LINE_WIDTH):
        circle(surface, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)