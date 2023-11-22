import pygame

# Initialize pygame
pygame.init()

# create a display surface and set its caption
WIDTH, HEIGHT = 600, 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Objects")

# Define colors as RGB tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# give a background color  to the display
display_surface.fill(BLUE)
# draw various shapes on our display
# line( surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0, 0), (100, 100), 5)
pygame.draw.line(display_surface, GREEN, (100, 100), (200, 300), 1)
# circle( surface, color, center, radius, thickness, 0 to fill  )
pygame.draw.circle(display_surface, WHITE, (WIDTH * 0.5, HEIGHT * 0.5), 200, 6)
pygame.draw.circle(display_surface, YELLOW, (WIDTH * 0.5, HEIGHT * 0.5 ), 195, 0)

# Rectangle( surface, color,  (top left x, top left y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100))
pygame.draw.rect(display_surface, MAGENTA, (500, 100, 50, 100))

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    
    # update the display
    pygame.display.update()

# end the game
pygame.quit()
