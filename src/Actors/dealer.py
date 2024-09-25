from .cards import Card
import time
class Dealer():
    def __init__(self, is_draw, count):
        self.is_draw = is_draw
        self.count = count
        self.ace_count = 0
        
    #checks if the first two cards equal to 21    
    def check_black_jack(self, card1, card2):
        if ((card1.get_value() + card2.get_value()) == 21):
            return True
    
    #adds to the count of the hand every time a new card is added
    def add_count(self, value):
        self.count += value
    
    def get_count(self):
        return self.count
    
    #checks if the count is over 21
    def check_bust(self):
        return self.count > 21
    
    def check_below_17(self):
        return self.count < 17
    
    def reset_count(self):
        self.count = 0
        
    def get_ace_count(self):
        return self.ace_count
    
    def increment_ace_count(self):
        self.ace_count += 1
    
    def adjust_for_ace(self):
        while self.get_ace_count() > 1:
            self.add_count(-10)
        return self.count
    
    