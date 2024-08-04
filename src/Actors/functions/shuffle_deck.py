from Actors.functions.load_images import load_images
from Actors.cards import Card
import random



def shuffle_deck():
    
    # Load card images
    card_image_deck = load_images("/Users/liyuxiao/Documents/CS/BlackJack/src/Assets/poker_cards/tile", 52, 60, 92)


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
    
    return card_deck