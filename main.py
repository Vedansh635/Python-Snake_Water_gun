# This is a simple implementation of the classic Snake, Water, Gun game
# between a user and a computer.
# The game randomly selects a move from the list [snake, water, gun]
# and the user is asked to input their move.
# The game then compares the two moves and determines a winner based on the
# rules of the game:
# - snake beats water
# - water beats gun
# - gun beats snake
# If the two moves are the same, the game is a draw.

import random

def game():
  # Ask the user for their move
  userchoice = input('Enter your move (s for snake, w for water, g for gun): ').lower()
  print('Your move:',userchoice)

  # Generate a random move for the computer
  computerchoice = str(random.choice(['s','w','g']))
  print('Computer move:',computerchoice)

  # Compare the two moves and determine the winner
  if userchoice==computerchoice:
      print('Draw._.')
  elif (userchoice == 's' and computerchoice== 'w') or (userchoice == 'w' and computerchoice== 'g') or (userchoice == 'g' and computerchoice=='s'):
     print('You win , Computer loss!!')
   # if user enters invalid move
  elif userchoice != 's' and userchoice != 'w' and userchoice != 'g':
     print('Invalid move. Please enter s, w, or g.')
  else:
     print('Computer win , you loss!')

# Call the game function
game()
