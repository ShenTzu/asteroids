from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        #print("here comes the pain")
        super().__init__(x, y, radius)
        pygame.draw.circle(self.image, "white",(radius, radius), radius, width = 2)
        self.rect = self.image.get_rect()
        self.rect.center = self.position 

    def update(self, dt):
        #print(self.velocity)
        self.position += self.velocity * dt
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def draw(self, screen):
        pygame.draw.circle(screen,"white", (self.radius, self.radius), self.radius, width = 2)