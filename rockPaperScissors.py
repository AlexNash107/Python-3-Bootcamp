# a simple game of rock paper scissors

import random

player1 = random.randint(1,3)

if player1 == 1:
    player1 = 'rock'
elif player1 == 2:
    player1 = 'paper'
elif player1 == 3:
    player1 = 'scissors'

player2 = input('Hello!  Rock Paper or Scissors? ').lower()
print('\n\n')

if player1 == player2:
    print("it's a tie!")
    
elif player1 == 'rock':
    if player2 == 'paper':
        print('Player 2 wins!')
    if player2 == 'scissors':
        print('Player 1 wins!')
        
elif player1 == 'paper':
    if player2 == 'rock':
        print('Player 1 wins!')
    if player2 == 'scissors':
        print('Player 2 wins!')

elif player1 == 'scissors':
    if player2 == 'rock':
        print('Player 2 wins!')
    if player2 == 'paper':
        print('Player 1 wins!')

else:
    print('Something went wrong....both players must select rock, paper, or scissors.....')
