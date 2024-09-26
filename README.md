# Project-Description


This is a simple implementation of the classic Snake,Water,Gun game with a twist! Instead of the traditional Rock, Paper, Scissors, this game uses Snake, Water, Gun as the three possible moves. The game is played between a user and a computer, where the computer's move is randomly generated.

# How to Play
1. Run the game by executing the `game()` function.
2. Enter your move by typing 's' for Snake, 'w' for Water, or 'g' for Gun.
3. The computer's move will be randomly generated and displayed.
4. The game will then compare the two moves and determine the winner based on the following rules:
- Snake beats Water
- Water beats Gun
- Gun beats Snake
- If both moves are the same, the game is a draw.

# Features
- Randomly generated computer move
- User input validation to ensure only valid moves are accepted
- Clear and concise output displaying the winner of each game

Code Overview
The code is written in Python and consists of a single function `game()` that contains the game logic. The function uses the `random` module to generate a random move for the computer, and the `input()` function to get the user's move. The game logic is implemented using simple if-elif-else statements to determine the winner.

# Feel free to modify or extend this code to add more features or improve the gameplay!
