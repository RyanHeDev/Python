import pygame

# Initialize pygame
pygame.init()

# create a display surface
WIDTH, HEIGHT = 600, 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blitting Images!")

# Create images this returns a surface object with the image drawn on it. we can then get the rect of the surface and use the rect to position the image
ninja_left_image = pygame.image.load("ninja.png")
ninja_left_rect = ninja_left_image.get_rect()
ninja_left_rect.topleft = (0, 0)
ninja_right_image = pygame.image.load("ninja.png")
ninja_right_rect = ninja_right_image.get_rect()
ninja_right_rect.topright = (WIDTH, 0)
# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # blit (copy) a surface object at the given coordinate
    display_surface.blit(ninja_left_image, ninja_left_rect)
    display_surface.blit(ninja_right_image, ninja_right_rect)
    
    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WIDTH, 75), 4)
    # update the display
    pygame.display.update()
            
# end the game
pygame.quit()
