# import pyttsx3
# engine = pyttsx3.init()
# engine.say("""
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# """)
# engine.runAndWait()

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 5

# Block settings
block_size = 50
block_speed = 5
num_blocks = 5

# Generate 5 red blocks with random positions
blocks = []
for _ in range(num_blocks):
    x = random.randint(0, WIDTH - block_size)
    y = random.randint(-400, -50)
    blocks.append([x, y])

# Clock for FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Update and draw each block
    for i in range(num_blocks):
        blocks[i][1] += block_speed

        # Reset block if it goes off screen
        if blocks[i][1] > HEIGHT:
            blocks[i][1] = random.randint(-200, -50)
            blocks[i][0] = random.randint(0, WIDTH - block_size)

        # Draw red block
        pygame.draw.rect(screen, RED, (blocks[i][0], blocks[i][1], block_size, block_size))

        # Collision detection
        if (player_x < blocks[i][0] + block_size and
            player_x + player_size > blocks[i][0] and
            player_y < blocks[i][1] + block_size and
            player_y + player_size > blocks[i][1]):
            print("Game Over!")
            running = False

    # Draw blue player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

