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
        self.points = points
        self.is_face_up = True
        
        
    #returns card value 
    def get_value(self):
        return self.points
    
    #shows card face down
    def show_face_down(self):
        self.image = self.face_down_image
        self.is_face_up = False
        
    #shows card face up
    def show_face_up(self):
        self.image = self.original_image
        self.is_face_up = True
        
    #flips orientation of card
    def flip(self):
        if self.is_face_up:
            self.show_face_down()
        else:
            self.show_face_up()
