import pygame
from Actors.functions.load_bg_image import set_screen_to_image
from Actors.functions.load_images import load_images
from Actors.cards import Card  # Ensure this import is correct
from Actors.button import Button
from Actors.player import Player
from Actors.dealer import Dealer
from Actors.functions.shuffle_deck import shuffle_deck


# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

bg = "/Users/liyuxiao/Documents/CS/BlackJack/src/Assets/board.png"
screen = pygame.display.set_mode((screen_width, screen_height))

set_screen_to_image(screen, bg)

# Set the title of the window
pygame.display.set_caption("BlackJack")


# Update the display
pygame.display.flip()

#make the card_deck 
card_deck = shuffle_deck()


#the buttons for the blackjack game
box_size = 75
draw_button = Button("hit", box_size, box_size, 150, 100 , "comicsans", (255,255,255), (0,0,0), (100,100,100))
stand_button = Button("stand", box_size, box_size, 150, 200 , "comicsans", (255,255,255), (0,0,0), (100,100,100))
double_button = Button("double", box_size, box_size, 150, 300 , "comicsans", (255,255,255), (0,0,0), (100,100,100))
split_button = Button("split", box_size, box_size, 150, 400 , "comicsans", (255,255,255), (0,0,0), (100,100,100))

button_group = [draw_button, stand_button, double_button, split_button]


#intialize player and dealer
player = Player(2500, True, 0)
dealer = Dealer(True, 0)

#list of player and dealers hand

player_hand = []
dealer_hand = []



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    for i in range(len(button_group)):
        button_group[i].draw(screen)
        button_group[i].update(pygame.mouse.get_pos())
        clickTrue = button_group[i].is_clicked(event)
        
        
        if(clickTrue):
            #check if the deck is empty
            if(len(card_deck) == 0):
                card_deck = shuffle_deck()
                
            if i == 0:
                drawn_card = card_deck.pop(0)
                player_hand.append(drawn_card)
                player.draw_card(screen, drawn_card, 300, 300+ len(player_hand)*100)
                #checks if player busted
                if(player.check_bust()):
                    #change val later
                    player.subtract_balance(500)
                    player_hand, dealer_hand = [], []
            elif i == 1:
                player.stand()
                while(dealer.check_below_17()):
                    drawn_card = card_deck.pop(0)
                    player_hand.append(drawn_card)
                    dealer.draw_card(screen,drawn_card, 300, 100+len(dealer_hand*10))
                if(dealer.check_bust()):
                    #if player wins, will change value later
                    player.add_balance(500)
                    player_hand, dealer_hand = [], []
                elif(dealer.get_count > player.get_count):
                    player.subtract_balance(500)
                    player_hand, dealer_hand = [], []
            elif i == 2:
                #double button
                player.set_bet(500)
                drawn_card = card_deck.pop(0)
                player_hand.append(drawn_card)
                player.draw_card(screen, drawn_card, 300, 300)
                
                if(player.check_bust):
                    #change val later
                    player.subtract_balance(500)
                    player_hand, dealer_hand = [], []
            else:
                if(player.split(card_deck[0], card_deck[0])):
                    player.set_bet(500)
             
                
            
            
            
    pygame.display.flip()

pygame.quit()
