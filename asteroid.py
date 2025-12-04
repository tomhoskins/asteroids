import circleshape
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from pygame.draw import circle

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface, color="white", width=LINE_WIDTH):
        circle(surface, color, self.position, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(0, 360)
        rotated_velocity = self.velocity.rotate(angle)
        neg_rotated_Velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = rotated_velocity * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = neg_rotated_Velocity * 1.2
