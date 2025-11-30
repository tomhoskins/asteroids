from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, LINE_WIDTH, PLAYER_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Player is a circle for hitbox, but looks like a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, color="white", line_width=LINE_WIDTH):
        pygame.draw.polygon(screen, color, self.triangle(), line_width)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
    
    def move(self, dt):
        # vector w/length of 1, from (0,0) to (0,1) (straight up)
        unit_vector = pygame.Vector2(0,1)

        # rotate vector by player's rotation, aligning it in the direction of the player
        rotated_vector = unit_vector.rotate(self.rotation)

        # scale vector by distance player should move (PLAYER_SPEED * dt)
        rotated_vector_with_speed = rotated_vector * PLAYER_SPEED * dt

        # Move the player by adding vector to position
        self.position += rotated_vector_with_speed