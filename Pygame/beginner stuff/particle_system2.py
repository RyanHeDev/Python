import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Particle System (Rectangles)")

# Define Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = random.randint(5, 10)
        self.height = self.width  # Make it a square for simplicity
        self.color = (255, 255, 255)
        self.speed = random.uniform(1, 3)
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        self.width -= 0.1
        self.height = self.width  # Keep it a square

# Create a list to hold particles
particles = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new particles
    mouse_x, mouse_y = pygame.mouse.get_pos()
    particles.append(Particle(mouse_x, mouse_y))

    # Update particles
    for particle in particles:
        particle.move()

    # Remove small particles
    particles = [particle for particle in particles if particle.width > 0]

    # Draw particles
    screen.fill((0, 0, 0))  # Clear the screen
    for particle in particles:
        pygame.draw.rect(screen, particle.color, (particle.x, particle.y, particle.width, particle.height))

    pygame.display.flip()  # Update the display

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
