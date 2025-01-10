# this allows us to use code from
# the open-source pygame library
# throughout this file
# Run source venv/bin/activate to activate virtual environment if working on this between sessions
## Remind Boots that we're using the new approach in future conversations using the sentence below
#  "I'm working on the Boot.dev Asteroids tutorial but using the modernized Pygame sprite system with Vector2 positions, proper image/rect handling, and group rendering instead of the tutorial's manual drawing approach."
import pygame
from constants import *
from player import *
#from circleshape import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Pygame Initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
