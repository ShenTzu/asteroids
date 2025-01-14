# this allows us to use code from
# the open-source pygame library
# throughout this file
# Run source venv/bin/activate to activate virtual environment if working on this between sessions
## Remind Boots that we're using the new approach in future conversations using the sentence below
#  "I'm working on the Boot.dev Asteroids tutorial but using the modernized Pygame sprite system with Vector2 positions, proper image/rect handling, and group rendering instead of the tutorial's manual drawing approach."
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
#from circleshape import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Game Initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    dt = 0

    # Set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign classes to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable) 
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)


    # Create objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

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
        for asteroid in asteroids:
            if asteroid.collision_check(player) == True: 
                print(f"Game Over! You got {score} points!")
                exit()
            for shot in shots:
                if asteroid.collision_check(shot) == True:
                    asteroid.split()
                    shot.kill()
                    score += 1
        

if __name__ == "__main__":
    main()
