import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, width, height, location_x, location_y, image, points, face_down_image, card_type):
        super().__init__()
        # Directly use the provided image
        self.original_image = pygame.transform.scale(image, (width, height))
        self.face_down_image = pygame.transform.scale(face_down_image, (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(location_x, location_y))
        self.card_type = card_type
        self.points = points  # This can be an int or a list [1, 11] for Aces
        self.is_face_up = True
        
    def get_card_type(self):
        return self.card_type

    # Returns the card value, handling the Ace's dual value
    def get_value(self, ace_high=True):
        if isinstance(self.points, list):  # Check if points is a list (for Aces)
            return self.points[1] if ace_high else self.points[0]
        return self.points
    
    # Shows card face down
    def show_face_down(self):
        self.image = self.face_down_image
        self.is_face_up = False
        
    # Shows card face up
    def show_face_up(self):
        self.image = self.original_image
        self.is_face_up = True
        
    # Flips orientation of card
    def flip(self):
        if self.is_face_up:
            self.show_face_down()
        else:
            self.show_face_up()
