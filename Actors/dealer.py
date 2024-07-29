import pygame
from .cards import Card

class Dealer():
    def __init__(self, is_draw, count):
        self.is_draw = is_draw
        self.count = count
        
        
    def check_black_jack(self, card1, card2):
        if ((card1.get_value() + card2.get_value()) == 21):
            return True
    
    def add_count(self, value):
        return (self.count + value)
    
    
    def draw_card(self, screen, card, x, y):
        print(f"Drawing card: {card}, type: {type(card)}")
        if isinstance(card, Card):
            print(f"Card value: {card.get_value()}")
            screen.blit(card.image, (x, y))
            self.add_count(card.get_value())
        else:
            print("Error: The object is not a Card instance.")