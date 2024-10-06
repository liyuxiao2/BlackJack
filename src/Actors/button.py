import pygame

class Button:
    def __init__(self, text, width, height, x, y, font, bg_color, text_color, hover_color, image=None):
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.is_hovered = False
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha() if image else None  # Load image if provided
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))  # Resize the image to button size
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)  # Support transparency
        self.rect = self.surface.get_rect(topleft=(x, y))
        self.render_text()

    def render_text(self):
        # If using an image, draw the image and apply hover effect
        if self.image:
            self.surface.blit(self.image, (0, 0))  # Draw the image
            if self.is_hovered:
                # Apply a semi-transparent overlay to show hover effect
                overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 100))  # White transparent overlay
                self.surface.blit(overlay, (0, 0))
        else:
            # If not using an image, change background color based on hover state
            self.surface.fill(self.hover_color if self.is_hovered else self.bg_color)
        
        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def update(self, mouse_pos):
        # Check if the mouse is hovering over the button
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.render_text()

    def draw(self, surface):
        # Draw the button surface onto the provided surface
        surface.blit(self.surface, self.rect.topleft)