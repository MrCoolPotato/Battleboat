# Battleship Game

Welcome to the Battleship Game! This is a single-player version of the classic board game where you can play against an AI. The game is developed using Python and Pygame.

## Features

- **Single-player mode:** Play against an AI opponent.
- **Various ship types:** Includes different types of ships like rectangles, squares, and carriers.
- **Graphical interface:** Developed using Pygame for an interactive experience.
- **AI logic:** The AI attempts to guess the orientation of your ships after a successful hit.
- **Toggle enemy ship visibility:** For development, you can see enemy ships. In production, they can be hidden.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/battleship-game.git
   cd battleship-game
   ```

2. **Create a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the game:**

   ```sh
   python main.py
   ```

2. **Game Controls:**
   - Use the mouse to click on the AI's board to attack.
   - The left board is your board, and the right board is the AI's board.

## Development

### Project Structure

```
battleship_game/
├── README.md
├── requirements.txt
├── main.py
├── battleship/
│   ├── __init__.py
│   ├── board.py
│   ├── ship.py
│   ├── game.py
│   ├── player.py
│   ├── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_board.py
│   ├── test_ship.py
│   ├── test_game.py
│   ├── test_player.py
│   ├── test_utils.py
└── assets/
    ├── battleship_icon.png
    └── other_assets/
```

### Important Files

- **main.py:** Entry point for the game.
- **battleship/board.py:** Contains the Board class to manage the game board.
- **battleship/ship.py:** Contains the Ship class to manage ships.
- **battleship/game.py:** Contains the Game class to manage the game logic.
- **battleship/player.py:** Contains the Player class to manage player actions.
- **battleship/utils.py:** Contains utility functions used across the game.

## Configuration

You can toggle the visibility of enemy ships by changing the `show_enemy_ships` parameter in the `Game` class:

```python
# main.py
from battleship.game import Game

if __name__ == "__main__":
    game = Game(show_enemy_ships=True)  # Set to False for production
    game.start()
```
