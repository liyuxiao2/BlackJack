import pygame

class Button:
    def __init__(self, text, width, height, x, y, font, bg_color, text_color, hover_color):
        self.surface = pygame.Surface((width, height))
        self.text = text
        self.font = pygame.font.SysFont(font, 24)  # Use a default size if not provided
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.is_hovered = False
        self.rect = self.surface.get_rect(topleft=(x, y))  # Corrected line
        self.render_text()
        
    #shows text for the button
    def render_text(self):
        self.surface.fill(self.hover_color if self.is_hovered else self.bg_color)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(text_surface, text_rect)
        
    #returns if clicked
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
    
    #shows if mouse hovers over button
    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        self.render_text()
        
    #creates button
    def draw(self, surface):
        surface.blit(self.surface, self.rect.topleft)