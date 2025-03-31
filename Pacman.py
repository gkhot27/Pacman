import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pac-Man")

# Player starting position and speed
x, y, speed = 200, 150, 3  #  speed for smoother movement

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Handle key presses
    keys = pygame.key.get_pressed()
    x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
    y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed

    # Keep the player within the screen boundaries
    x = max(15, min(x, 385))  # Prevents going off-screen horizontally
    y = max(15, min(y, 285))  # Prevents going off-screen vertically

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player (yellow circle)
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 15)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS (slows down the game)
    clock.tick(30)
