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

# Particle class
class Particle:
    def __init__(self, x, y):
        # Initialize particle properties here
        self.x = x
        self.y = y
        self.width = random.randint(5, 10)
        self.height = self.width
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.color = (self.r, self.g, self.b)
        self.speed = random.uniform(1, 3)
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self):
        # Update particle position and size here
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)
        self.width -= 0.1
        self.height = self.width

# List to hold particles
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
    particles_to_remove = [particle for particle in particles if particle.width < 0]
    for particle in particles_to_remove:
        particles.remove(particle)

    screen.fill((0, 0, 0))
    
    # Draw particles
    for particle in particles:
        pygame.draw.rect(screen, particle.color, (particle.x, particle.y, particle.width, particle.height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
