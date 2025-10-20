import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pos_x, pos_y = self.position.x, self.position.y
        old_radius = self.radius
        old_velocity = self.velocity

        self.kill()
        

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        v1 = old_velocity.rotate(random_angle)
        v2 = old_velocity.rotate(-random_angle)

        a1 = Asteroid(pos_x, pos_y, new_radius)
        a2 = Asteroid(pos_x, pos_y, new_radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2

        


