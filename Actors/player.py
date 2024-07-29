from .dealer import Dealer
from .cards import Card
'''
Player Class

User gets option to hit, stand, double, or split

User starts off with a set balance, if balance goes to zero, game is over
'''
class Player(Dealer):
    def __init__(self, balance, is_draw, count):
        super().__init__(is_draw, count)
        self.balance = balance
        
    def stand(self):
        #stand aka do not take any more cards
        return None
    
    def double(self):
        return None
    
    def split(self, card1, card2):
        if (card1.get_card_type == card2.get_card_type):
            return True
    
    
    def get_balance(self):
        return self.balance
    
    def add_balance(self, amount):
        return self.balance + amount
    
    def subtract_balance(self, amount):
        return self.balance - amount
    
    def check_game_over(self):
        if self.get_balance() == 0:
            return True
        return False
    
    
        
    
    