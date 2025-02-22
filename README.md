# Tic Tac Toe Game

## Description
This is a simple Tic Tac Toe game built using Python and Tkinter for the graphical user interface. The game supports two modes:
- **Single Player Mode**: Play against an AI opponent using the Minimax algorithm.
- **Two Player Mode**: Play against another human on the same computer.

## Features
- **Graphical User Interface (GUI)** using Tkinter
- **Single Player Mode** with AI opponent (Minimax Algorithm)
- **Two Player Mode** for local multiplayer
- **Game restart functionality**
- **Dynamic UI updates**
- **Winner and Draw detection**

## Installation
Ensure you have Python installed on your system. If not, download and install it from [Python.org](https://www.python.org/downloads/).

## How to Run
1. Download or clone this repository.
2. Navigate to the project directory.
3. Run the script using:
   ```bash
   python tictae.py
   ```

## How to Play
- Select the game mode by clicking either **Single Player Mode** or **2-player Mode**.
- Click on an empty square to make a move.
- The game will alternate turns between 'X' and 'O'.
- In Single Player Mode, the AI will play as 'O'.
- The game will display a message when a player wins or if the game ends in a draw.
- Click the **Restart Game** button to start a new match.

## Game Logic
### Winning Conditions
The game checks the following conditions for a win:
- Any row (horizontal win)
- Any column (vertical win)
- Any diagonal (diagonal win)

### AI Strategy
The AI uses the **Minimax algorithm** to make the best possible move, ensuring an optimal challenge for the player.

## Future Improvements
- Add sound effects
- Improve UI design
- Implement difficulty levels for AI
- Add online multiplayer functionality

## License
This project is licensed under the MIT License.

## Author
Developed by Pham Nguyen Viet Tri. Feel free to contribute and improve the game!

---
