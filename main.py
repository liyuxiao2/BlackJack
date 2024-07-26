import pygame
from Actors.functions.load_bg_image import set_screen_to_image
# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

bg = "/Users/liyuxiao/Documents/CS/BlackJack/Assets/board.png"
screen = pygame.display.set_mode((screen_width, screen_height))

set_screen_to_image(screen, bg)

# Set the title of the window
pygame.display.set_caption("BlackJack")


# Update the display
pygame.display.flip()

# Game loop
running = True


while running:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
