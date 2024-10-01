 <br /> <div align="center"><strong>Blackjack Game</strong></div> <div align="center">A simple Blackjack game with Hit, Stand, and Double options, built using Pygame</div> <br /> <div align="center"> <!-- Python Version --> <a href="https://www.python.org/downloads/"> <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version" /> </a> <!-- Pygame Dependency --> <a href="https://www.pygame.org/wiki/GettingStarted"> <img src="https://img.shields.io/badge/Pygame-2.x-green.svg" alt="Pygame Version" /> </a> <!-- License --> <a href="#license"> <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="MIT License" /> </a> </div> <br /> <div align="center"> <sub>Created by <a href="https://github.com/liyuxiao2">Liyu</a></sub> </div>
Features
<dl> <dt>Hit</dt> <dd>Draw another card to increase your hand value.</dd> <dt>Stand</dt> <dd>Keep your current hand and let the dealer play.</dd> <dt>Double</dt> <dd>Double your bet and receive exactly one more card.</dd> </dl>
Requirements
Python 3.x
Pygame 2.x
You can install Pygame using pip:

bash
Copy code
pip install pygame
How to Run
Clone or download the repository.
Navigate to the game directory in your terminal.
Run the game using:
bash
Copy code
python blackjack.py
How to Play
Both the dealer and the player start with two cards.
Choose one of the three actions:
Hit: Draw an additional card.
Stand: Keep your current hand and let the dealer play.
Double: Double your bet and receive one more card.
The goal is to get as close to 21 as possible without going over. If your hand exceeds 21, you lose the round.
After the player ends their turn, the dealer will play according to Blackjack rules.
You win by having a higher hand total than the dealer without busting (going over 21).
License
This project is licensed under the MIT License. Feel free to modify and distribute the code as you like.
