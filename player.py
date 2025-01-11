from constants import *
from circleshape import *

class Player(CircleShape):

    #containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.image = pygame.Surface([radius * 2, radius * 2],pygame.SRCALPHA)
        #pygame.draw.circle(self.image, "white",(radius, radius), radius, width = 2)
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.rect.center = self.position
        self.original_image = self.image
        pygame.draw.polygon(self.image,"white",self.triangle(), width = 2)
        self.rect = self.image.get_rect()
        self.rect.center = self.position 

    # in the player class
    def triangle(self):
        center = pygame.Vector2(self.radius, self.radius)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), width = 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

        # Rotate the original image
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        # Update rect to maintain center position
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # Update rect position to match Vector2 position
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

   