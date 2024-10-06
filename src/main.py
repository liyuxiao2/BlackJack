import pygame
from Actors.functions.load_bg_image import set_screen_to_image
from Actors.button import Button
from Actors.player import Player
from Actors.dealer import Dealer
from Actors.functions.shuffle_deck import shuffle_deck

# Initialize Pygame
pygame.init()

# Initialize the font for the game 
game_font = pygame.font.Font('/Users/liyuxiao/Documents/CS/SideProjects/BlackJack/src/Assets/game_font.ttf', 20)


# Set the dimensions of the screen
screen_width = 800
screen_height = 600

bg = "/Users/liyuxiao/Documents/CS/SideProjects/BlackJack/src/Assets/board.png"
screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)

set_screen_to_image(screen, bg)

# Set the title of the window
pygame.display.set_caption("BlackJack")

time_interval = 200

# Make the card_deck 
card_deck = shuffle_deck()

# The buttons for the blackjack game
big_button_img = "/Users/liyuxiao/Documents/CS/SideProjects/BlackJack/src/Assets/bigButton.png"
small_button_img = "/Users/liyuxiao/Documents/CS/SideProjects/BlackJack/src/Assets/smallButton.png"
box_size = 75
draw_button = Button("hit", box_size, box_size, 150, 100, game_font, (255, 255, 255), (0, 0, 0), (100, 100, 100), big_button_img )
stand_button = Button("stand", box_size, box_size, 150, 200, game_font, (255, 255, 255), (0, 0, 0), (100, 100, 100), big_button_img)
double_button = Button("double", box_size, box_size, 150, 300, game_font, (255, 255, 255), (0, 0, 0), (100, 100, 100), big_button_img)
increase_bet_button = Button("+ 100", box_size+50, box_size, 100, 400, game_font, (255, 255, 255), (0, 0, 0), (100, 100, 100), big_button_img)
decrease_bet_button = Button("- 100", box_size+50, box_size, 250, 400, game_font, (255, 255, 255), (0, 0, 0), (100, 100, 100), big_button_img)

button_group = [draw_button, stand_button, double_button, increase_bet_button, decrease_bet_button]
 
# Initialize player and dealer
player = Player(2500, True, 0)
dealer = Dealer(True, 0)

bet_size = 100



# List of player and dealer's hand, purely for displaying the cards on screen
player_hand = []
dealer_hand = []
hand_over = False


def stand():
    # Reveal the dealer's hidden card
        show_hidden_card()
        render_all()
        pygame.time.delay(time_interval)

        # Dealer draws cards until reaching 17 or more
        while dealer.check_below_17():
            draw_card(dealer_hand, dealer)
            render_all()
            pygame.time.delay(time_interval)  # Pause between each dealer card draw

        # Dealer's hand is now fully revealed
        if dealer.check_bust():
            player.add_balance()
            render_text("Dealer busts, you win!")
            render_all()
            pygame.display.flip()
            pygame.time.delay(time_interval)
        else:
            # Compare dealer's and player's hand
            dealer_total = dealer.get_count()
            player_total = player.get_count()

            if dealer_total > player_total:
                player.subtract_balance()
                render_text("Dealer wins!")
                pygame.display.flip()
                pygame.time.delay(time_interval)
            elif dealer_total < player_total:
                player.add_balance()
                render_text("Player wins!")
                pygame.display.flip()
                pygame.time.delay(time_interval)
            else:
                render_text("It's a tie!")
                pygame.display.flip()
                pygame.time.delay(time_interval)
                
def draw():
    draw_card(player_hand, player)
    render_all()  # Redraw the entire screen after a hit
    pygame.time.delay(time_interval)  # Pause for time_interval ms after drawing a card

    # Check if player busted
    if player.check_bust():
        player.subtract_balance()
        render_text("Player busts, you lose!")
        hand_over = True
                        
def adjust_for_aces(user):
    """Adjust the value of Aces in hand if the total exceeds 21."""
    # While the count is above 21 and there's an Ace treated as 11, reduce its value to 1
    while user.get_count() > 21 and user.get_ace_count() > 1:
        user.adjust_for_ace()  # This method should reduce an Ace value from 11 to 1

def draw_card(deck_to_add_to, user, face_down = False):
    """Draw a card from the deck for the player or dealer."""
    drawn_card = card_deck.pop(0)
    if drawn_card.get_card_type() == "Ace":
        user.increment_ace_count()
    
    if face_down == True:
        drawn_card.show_face_down()
        deck_to_add_to.append(drawn_card)
    else:
        card_value = drawn_card.get_value()
        user.add_count(card_value)
        deck_to_add_to.append(drawn_card)
    
    # Adjust for Aces if necessary (e.g., switching 11 to 1 if total exceeds 21)
    adjust_for_aces(user)

def reset_board():
    """Reset the board and clear hands."""
    player_hand.clear()
    dealer_hand.clear()
    player.reset_count()
    dealer.reset_count()
    start()

def render_count():
    """Render player and dealer counts."""
    player_balance_label = game_font.render("Balance: " + str(player.get_balance()), True, (255,255,255))
    bet_label = game_font.render("Bet size: " + str(player.get_bet()), True, (255,255,255))
    player_count_label = game_font.render("Player: " + str(player.get_count()), True, (255, 255, 255))
    dealer_count_label = game_font.render("Dealer: " + str(dealer.get_count()), True, (255, 255, 255))
    screen.blit(player_count_label, (600, 300))
    screen.blit(dealer_count_label, (600, 100))
    screen.blit(player_balance_label, (0,0))
    screen.blit(bet_label, (550, 0))    

def render_text(text):
    """Render text on the screen."""
    label_text = game_font.render(text, True, (255, 255, 255))
    screen.blit(label_text, (600, 200))

def render_all():
    """Redraw the entire screen: background, buttons, cards, and counts."""
    set_screen_to_image(screen, bg)
    
    # Draw buttons
    for button in button_group:
        button.draw(screen)
    
    # Draw player and dealer hands
    for i, card in enumerate(player_hand):
        screen.blit(card.image, (300 + i * 20, 300))
    for i, card in enumerate(dealer_hand):
        screen.blit(card.image, (300 + i * 20, 100))
    
    # Render the player and dealer counts
    render_count()
    
    # Update the display
    pygame.display.flip()




#gives the starting hand for both dealer and player
def start():
    for i in range(2):
        draw_card(player_hand, player)
    
    #draw for dealer
    draw_card(dealer_hand, dealer)
    draw_card(dealer_hand, dealer, True)
    render_all()  # Redraw the entire screen after a hit


def show_hidden_card():
    hidden_card = dealer_hand[1]
    
    hidden_card.show_face_up()
    
    dealer_hand[1] = hidden_card
    
    card_val = hidden_card.get_value()
    
    dealer.add_count(card_val)
    
    
    
def play(button, hand_over, card_deck):
    global bet_size
    # Handle button clicks
    if len(card_deck) == 0:
        card_deck = shuffle_deck()

    # Hit button (Player draws a card)
    if button == draw_button:
        draw()
    # Stand button (Player stands, dealer reveals cards)
    elif button == stand_button:
        stand()
        hand_over = True
    # Double button (Player doubles their bet and draws one last card)
    elif button == double_button:
        player.double()
        draw()
        stand()
        hand_over = True
            
            
    elif button == increase_bet_button:
        if(player.check_bet_size(bet_size+100) == True):
            bet_size += 100
            player.set_bet(bet_size)
        render_all()
    elif button == decrease_bet_button:
        if(bet_size >= 100):
            bet_size -= 100
            player.set_bet(bet_size)
        render_all()
        

    # If the hand is over, reset the game
    if hand_over:
        pygame.time.delay(2000)  # Wait 2 seconds before resetting
        reset_board()
        render_all()
        

    
# Game loop
running = True

render_all()
start()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in button_group:
            button.update(pygame.mouse.get_pos())
            if button.is_clicked(event):
                play(button, hand_over, card_deck)

pygame.quit()
