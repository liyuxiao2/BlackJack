import pygame
from Actors.functions.load_bg_image import set_screen_to_image
from Actors.functions.load_images import load_images
from Actors.cards import Card  # Ensure this import is correct
from Actors.button import Button
from Actors.player import Player
from Actors.dealer import Dealer

import random
import time


# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600

bg = "/Users/liyuxiao/Documents/CS/BlackJack/Assets/board.png"
screen = pygame.display.set_mode((screen_width, screen_height))

set_screen_to_image(screen, bg)

# Set the title of the window
pygame.display.set_caption("BlackJack")


# Update the display
pygame.display.flip()

# Load card images
card_image_deck = load_images("/Users/liyuxiao/Documents/CS/BlackJack/Assets/poker_cards/tile", 52, 60, 92)


#load all the card objects
card_possibilities = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card_deck = []
point_counter = 1

for i in range(51):
    # Create a card object for each image in the deck
    card_deck.append(Card(width=71, height=96, location_x=200, location_y=200,
                          image=card_image_deck[i], points=point_counter % 13 + 1,  # Calculate points
                          face_down_image = card_image_deck[51], card_type = card_possibilities[point_counter%13]))  # Use a separate face-down image
    point_counter += 1  # Increment point counter for each card (adjust if needed)

random.shuffle(card_deck)


print(card_deck[0].get_value()) 

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
            if i == 0:
                player.draw_card(screen, card_deck.pop(0), 300, 300 )
            elif i == 1:
                player.stand()
            elif i == 2:
                player.draw_card(screen, card_deck.pop(0), 300, 300)
            else:
                player.split(card_deck[0], card_deck[0])
                
                
            
            
            
    pygame.display.flip()

pygame.quit()
