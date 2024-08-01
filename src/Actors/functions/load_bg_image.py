import pygame

def set_screen_to_image(screen, image_path):
  """Sets the entire Pygame screen to the specified image.

  Args:
    screen: The Pygame display surface.
    image_path: The path to the image file.
  """

  background_image = pygame.image.load(image_path)
  background_image = pygame.transform.scale(background_image, screen.get_size())
  screen.blit(background_image, (0, 0))
  pygame.display.flip()