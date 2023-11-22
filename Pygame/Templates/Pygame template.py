import pygame

# Initialize pygame
pygame.init()

# Create a display surface and set its caption
WIDTH, HEIGHT = 600, 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT ))
pygame.display.set_caption("Hello World")

# Main game loop
running = True
while running:
    # loop through a list of event objects that have occured
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
