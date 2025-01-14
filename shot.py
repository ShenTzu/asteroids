from constants import *
from circleshape import *

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.draw.circle(self.image, "white",(self.image.get_width()/2, self.image.get_width()/2), radius, width = 5)
        #self.rect = self.image.get_rect()
        #self.rect.center = self.position 

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y