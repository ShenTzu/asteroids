from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        #print("here comes the pain")
        super().__init__(x, y, radius)
        pygame.draw.circle(self.image, "white",(self.image.get_width()/2, self.image.get_width()/2), radius, width = 2)
        #self.rect = self.image.get_rect()
        #self.rect.center = self.position 

    def update(self, dt):
        #print(self.velocity)
        self.position += self.velocity * dt
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def draw(self, screen):
        pygame.draw.circle(screen,"white", (self.radius, self.radius), self.radius, width = 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        angle = random.uniform(20,50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2 * 1.2
        
