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
        self.bet = 100              
        
    def get_balance(self):
        return self.balance
    
    
    def double(self):
        self.set_bet(self.get_bet()*2)
    
    def split(self, card1, card2):
        if(isinstance(card1,Card) and isinstance(card2, Card)):
            if (card1.get_card_type == card2.get_card_type):
                return True
    
    #sets the bet for the player
    def set_bet(self, amount_to_bet):
        #check if you have enough in the balance to bet
        self.bet = amount_to_bet
    
    
    def check_bet_size(self, amount_to_bet):
        if(self.balance - amount_to_bet >= 0):
            return(True)
        else:
            return (False)

    
    def get_bet(self):
        return self.bet
        
    
    #adds to the balance after a win
    def add_balance(self):
        self.balance += self.bet
    
    #subtracts balance after a loss
    def subtract_balance(self):
        self.balance -= self.bet
    
    
    #check if your balance is 0
    def check_game_over(self):
        if self.balance == 0:
            return True
        return False
    
    
        
    
    