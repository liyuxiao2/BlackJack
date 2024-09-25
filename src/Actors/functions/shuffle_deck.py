from Actors.functions.load_images import load_images
from Actors.cards import Card
import random

def shuffle_deck():
    
    # Load card images
    card_image_deck = load_images("/Users/liyuxiao/Documents/CS/SideProjects/BlackJack/src/Assets/poker_cards/tile", 53, 60, 92)


    # Load all the card objects
    card_possibilities = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_deck = []

    for i in range(52):
        # Calculate points
        if i % 13 == 0:
            points = [1, 11]  # Ace can be 1 or 11
        elif i % 13 >= 10:
            points = 10  # Face cards (Jack, Queen, King)
        else:
            points = (i % 13) + 1  # Number cards 2-10

        # Create a card object for each image in the deck
        card_deck.append(Card(
            width=71, 
            height=96, 
            location_x=200, 
            location_y=200,
            image=card_image_deck[i], 
            points=points,  # Set points based on the card type
            face_down_image=card_image_deck[52], 
            card_type=card_possibilities[i % 13]  # Assign card type based on the index
        ))

    random.shuffle(card_deck)
    
    return card_deck
