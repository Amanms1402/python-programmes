import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elliptical Orbits Simulation")

# Function to calculate the position of an object in an elliptical orbit
def calculate_position(a, b, angle):
    x = a * math.cos(math.radians(angle))
    y = b * math.sin(math.radians(angle))
    return int(x), int(y)

# Main function to run the simulation
def main():
    clock = pygame.time.Clock()
    running = True
    angle = 0

    # Semi-major and semi-minor axes of the ellipse
    a = 300
    b = 200

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Calculate the position of the object in the elliptical orbit
        x, y = calculate_position(a, b, angle)

        # Draw the orbit
        pygame.draw.ellipse(screen, WHITE, (SCREEN_WIDTH//2 - a, SCREEN_HEIGHT//2 - b, 2*a, 2*b), 1)

        # Draw the object
        pygame.draw.circle(screen, WHITE, (SCREEN_WIDTH//2 + x, SCREEN_HEIGHT//2 + y), 5)

        pygame.display.flip()
        angle += 1  # Increment the angle for animation
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
