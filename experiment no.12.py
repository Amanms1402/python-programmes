import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
GRAVITY = 0.5
BOUNCE_FACTOR = 0.8

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")

# Ball properties
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Apply gravity
    ball_speed_y += GRAVITY

    # Check for collision with walls
    if ball_x <= BALL_RADIUS or ball_x >= SCREEN_WIDTH - BALL_RADIUS:
        ball_speed_x *= -1

    if ball_y <= BALL_RADIUS or ball_y >= SCREEN_HEIGHT - BALL_RADIUS:
        ball_speed_y *= -BOUNCE_FACTOR

    # Draw background
    screen.fill(BG_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()
