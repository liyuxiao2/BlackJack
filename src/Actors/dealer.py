from .cards import Card
import time
class Dealer():
    def __init__(self, is_draw, count):
        self.is_draw = is_draw
        self.count = count
        
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
        if self.count > 21:
            return True
        return False
    
    def check_below_17(self):
        if(self.count < 17):
            return True
        return False
    
    def reset_count(self):
        self.count = 0
    
    #draws an additional card into the hand
    def draw_card(self, screen, card, x_location, y_location):
        #check if still needing to draw
        if(self.is_draw):
            print(f"Drawing card: {card}, type: {type(card)}")
            #have to check whether the objects we are dealing with are from the card class
            if isinstance(card, Card):
                time.sleep(0.5)
                print(f"Card value: {card.get_value()}")
                screen.blit(card.image, (x_location, y_location))
                print("total: " + str(self.count))
            else:
                print("Error: The object is not a Card instance.")