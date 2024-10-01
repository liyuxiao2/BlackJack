<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <h1> BlackJack </h1>
</head>
<body>

  
  <br />

  <div style="text-align: center;">
    <p>A simple Blackjack game with Hit, Stand, and Double options, built using Pygame</p>
  </div>

  <br />

  <div style="text-align: center;">
    <a href="https://www.python.org/downloads/">
      <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version" />
    </a>
    <a href="https://www.pygame.org/wiki/GettingStarted">
      <img src="https://img.shields.io/badge/Pygame-2.x-green.svg" alt="Pygame Version" />
    </a>
    <a href="#license">
      <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="MIT License" />
    </a>
  </div>

  <br />

  <div style="text-align: center;">
    <sub>Created by <a href="https://github.com/liyuxiao2">Liyu Xiao</a></sub>
  </div>

  <h2>Features</h2>
  <dl>
    <dt><strong>Hit</strong></dt>
    <dd>Draw another card to increase your hand value.</dd>

    <dt><strong>Stand</strong></dt>
    <dd>Keep your current hand and let the dealer play.</dd>

    <dt><strong>Double</strong></dt>
    <dd>Double your bet and receive exactly one more card.</dd>
  </dl>

  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>Pygame 2.x</li>
  </ul>
  <p>You can install Pygame using pip:</p>
  <pre><code>pip install pygame</code></pre>

  <h2>How to Run</h2>
  <ol>
    <li>Clone or download the repository.</li>
    <li>Navigate to the game directory in your terminal.</li>
    <li>Run the game using:</li>
    <pre><code>python blackjack.py</code></pre>
  </ol>

  <h2>How to Play</h2>
  <ol>
    <li>Both the dealer and the player start with two cards.</li>
    <li>Choose one of the three actions:
      <ul>
        <li><strong>Hit</strong>: Draw an additional card.</li>
        <li><strong>Stand</strong>: Keep your current hand and let the dealer play.</li>
        <li><strong>Double</strong>: Double your bet and receive one more card.</li>
      </ul>
    </li>
    <li>The goal is to get as close to 21 as possible without going over. If your hand exceeds 21, you lose the round.</li>
    <li>After the player ends their turn, the dealer will play according to Blackjack rules.</li>
    <li>You win by having a higher hand total than the dealer without busting (going over 21).</li>
  </ol>

  <h2 id="license">License</h2>
  <p>This project is licensed under the MIT License. Feel free to modify and distribute the code as you like.</p>

</body>
</html>
