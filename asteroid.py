import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) :
        self.position += self.velocity * dt

    def split(self):
        if (self.radius <= ASTEROID_MIN_RADIUS):
            pass
        else:
            log_event("asteroid_split")
            r = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            v1 = self.velocity.rotate(r)
            v2 = self.velocity.rotate(r * -1)
            a1 = Asteroid(self.position[0], self.position[1], new_radius)
            a2 = Asteroid(self.position[0], self.position[1], new_radius)
            a1.velocity = v1 * 1.2
            a2.velocity = v2 * 1.2
        self.kill()
