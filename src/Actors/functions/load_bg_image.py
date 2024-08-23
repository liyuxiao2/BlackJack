import pygame

def set_screen_to_image(screen, image_path, area=None):
    """Sets the Pygame screen to the specified image, or to a specific area if provided.

    Args:
        screen: The Pygame display surface.
        image_path: The path to the image file.
        area: A pygame.Rect object that specifies the area to update. If None, the entire screen is updated.
    """
    # Load and scale the image
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, screen.get_size())

    if area is not None:
        # Blit only the specified area
        screen.blit(background_image, area, area)
    else:
        # Blit the entire image if no area is specified
        screen.blit(background_image, (0, 0))
    
    pygame.display.flip()
