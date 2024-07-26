import pygame


face_down = "/Users/liyuxiao/Documents/CS/BlackJack/Assets/poker_cards/tile52.png"
class Card:
    def __init__(self, width, height, location_x, location_y, image, points, face_down_image_path, card_type):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(location_x, location_y))
        self.points = points
        self.card_type = card_type
        self.face_down_image = pygame.image.load(face_down_image_path)
        self.face_down_image = pygame.transform.scale(self.face_down_image, (width, height))
        
    def get_value(self):
        return self.points
    
    def show_face_down(self):
        #return image that is face down
        self.image = self.face_down_image
        
    def get_card_type(self):
        return self.card_type