import pygame 

pygame.init()

WIDTH, HEIGHT = 600, 300
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blitting Images")

# define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

"""
# see all available system fonts
fonts = pygame.font.get_font()
for font in fonts:
    print(font)
"""

# define fonts
system_font = pygame.font.SysFont("calibri", 64)
costum_font = pygame.font.Font("DangerNightPersonal.otf", 32)

# define text
system_text = system_font.render(" Danger Night", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (WIDTH * 0.5, HEIGHT * 0.5)
costum_text = costum_font.render("TAB PROGRAMMER",True, GREEN)
costum_text_rect = costum_text.get_rect()
costum_text_rect.center = (WIDTH * 0.5, HEIGHT *0.5 + 100)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # blit (copy) the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(costum_text, costum_text_rect)
    
    #update the display
    pygame.display.update()
    


pygame.quit()
