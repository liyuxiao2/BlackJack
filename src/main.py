import pygame
import time
from Actors.functions.load_bg_image import set_screen_to_image
from Actors.functions.load_images import load_images
from Actors.cards import Card  # Ensure this import is correct
from Actors.button import Button
from Actors.player import Player
from Actors.dealer import Dealer
from Actors.functions.shuffle_deck import shuffle_deck

# Initialize Pygame
pygame.init()

# Initialize the font for the game 
game_font = pygame.font.Font(None, 55)

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

bg = "/Users/liyuxiao/Documents/CS/BlackJack/src/Assets/board.png"
screen = pygame.display.set_mode((screen_width, screen_height))

set_screen_to_image(screen, bg)

# Set the title of the window
pygame.display.set_caption("BlackJack")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Make the card_deck 
card_deck = shuffle_deck()

# The buttons for the blackjack game
box_size = 75
draw_button = Button("hit", box_size, box_size, 150, 100, "comicsans", (255, 255, 255), (0, 0, 0), (100, 100, 100))
stand_button = Button("stand", box_size, box_size, 150, 200, "comicsans", (255, 255, 255), (0, 0, 0), (100, 100, 100))
double_button = Button("double", box_size, box_size, 150, 300, "comicsans", (255, 255, 255), (0, 0, 0), (100, 100, 100))
split_button = Button("split", box_size, box_size, 150, 400, "comicsans", (255, 255, 255), (0, 0, 0), (100, 100, 100))

button_group = [draw_button, stand_button, double_button, split_button]

# Initialize player and dealer
player = Player(2500, True, 0)
dealer = Dealer(True, 0)

# List of player and dealer's hand, this is purely for displaying the cards on screen
player_hand = []
dealer_hand = []

def draw_card(screen, deck_to_add_to, drawn_card, user, x ,y):
    drawn_card = card_deck.pop(0)
    if(drawn_card.get_card_type() == "Ace"):
        #check if the card should be 11 or 1, if the count is less than or more than 11                   
        if(user.get_count() + 11 > 21):
            card_value = drawn_card.get_value(False)
    card_value = drawn_card.get_value()
    
    #add to the player count
    time.sleep(0.1)
    user.add_count(card_value)
    deck_to_add_to.append(drawn_card)
    screen.blit(drawn_card.image, (x + len(deck_to_add_to) * 20,y))
    pygame.display.flip()

def reset_board(hand_1, hand_2):
    time.sleep(2)
    hand_1.clear()
    hand_2.clear()
    player.reset_count()
    dealer.reset_count()
    set_screen_to_image(screen, bg)
    
    
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle button clicks
    for i in range(len(button_group)):

            
        button_group[i].draw(screen)
        button_group[i].update(pygame.mouse.get_pos())
        clickTrue = button_group[i].is_clicked(event)
        
        if clickTrue:
            if len(card_deck) == 0:
                card_deck = shuffle_deck()
            
            # Hit button
            if i == 0:
                draw_card(screen, player_hand, card_deck.pop(0), player, 300, 300)
                
                # Check if player busted
                if player.check_bust():
                    player.subtract_balance(500)
                    reset_board(player_hand, dealer_hand)
                    
            # Stand button
            elif i == 1:
                while dealer.check_below_17():
                    draw_card(screen, dealer_hand, card_deck.pop(0), dealer, 300, 100)
                    
                    time.sleep(1)
                    
                if dealer.check_bust():
                    player.add_balance(500)
                if dealer.get_count() > player.get_count():
                    player.subtract_balance(500)
                reset_board(player_hand, dealer_hand)

            # Double button
            elif i == 2:
                player.set_bet(500)
                draw_card(screen, player_hand, card_deck.pop(0), player, 300, 300)
                
                if player.check_bust():
                    player.subtract_balance(500)
                    reset_board(player_hand, dealer_hand)

            # Split button
            else:
                if player.split(card_deck[0], card_deck[1]):
                    player.set_bet(500)
    
    # Clear and redraw the background in the label area
    label_area = pygame.Rect(600, 100, 200, 50)
    set_screen_to_image(screen, bg, area=label_area)
    
    # Calculate and render the player's hand value
    player_count_label = game_font.render(str(player.get_count()), True, (255, 255, 255))
    screen.blit(player_count_label, (600, 100))
    
    # Draw everything else on the screen before updating
    for button in button_group:
        button.draw(screen)
    
    
    # Update the display once everything is drawn
    pygame.display.flip()

    # Cap the frame rate at 60 FPSa
    clock.tick(60)

pygame.quit()
