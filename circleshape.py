import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        self.image = pygame.Surface([radius * 5, radius * 5],pygame.SRCALPHA)
        #self.image.fill((255, 0, 0, 128))
        #pygame.draw.circle(self.image, "white",(radius, radius), radius, width = 2)
        #self.rect = pygame.Rect(x, y, radius * 5, radius * 5)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, shape):
        distance = self.radius + shape.radius
        if self.position.distance_to(shape.position) < distance:
            return True
        else: return False